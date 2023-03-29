# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import click
import sys
from typing import List, Tuple, Optional
from pathlib import Path
import shutil
import logging

import numpy as np
import cv2

import pd.session
import pd.state
import pd.umd
from pd.core import PdError
from pd.assets import get_vehicle_wheel_poses, get_vehicle_wheel_names, get_wheel_radius
from pd.util import common_step_options, StepScriptContext


DEFAULT_LOCATION = ('SJ_237AndNorth1st', 'v2.0.2')
DEFAULT_LIGHTING = 'LS_sky_noon_partlyCloudy_1113_HDS024'
SIM_RATE_PER_SECOND = 100  # Our simulation runs at this rate
RENDER_FRAME_INTERVAL = 1  # Every Nth simulation state is rendered
CAPTURE_FRAME_INTERVAL = 10  # Every Nth render is saved/displayed
MAX_SIM_TIME_SEC = 20.0


def save_image(base_path: Path, sensor: str, frame: int, image):
    """
    Save cv2 image to disk
    Args:
        base_path: Base output directory path
        sensor: Name of sensor
        frame: Frame number
        image: CV2 image to save
    """
    image_path = base_path / sensor / f"{frame:06d}.png"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    click.echo(f"Saving image: {image_path}")
    cv2.imwrite(str(image_path), image)


def get_velocity(prev_pose: pd.state.Pose6D, curr_pose: pd.state.Pose6D, time_delta_sec: float) \
        -> Tuple[float, float, float]:
    """Get velocity vector from two displaced Poses and a time delta"""
    velocity = (np.array(curr_pose.translation) - np.array(prev_pose.translation)) / time_delta_sec
    return tuple(velocity)


def generate_route(
        umd_map,
        start_lane_segment_id: int
    ) -> List[Tuple[float, float, float]]:
    """
    Generates a route spanning driveable lane segments
    Args:
        umd_map: the Umd map object
        start_lane_segment_id: Id of the lane segment at which to start the route

    Returns:
        Generated route as a list of points
    """
    # Traverse lane segments starting at a hand-chosen lane for the Sunnyvale map
    # Simple traversal strategy: select the first successor lane
    route_points = []
    lane_segments_gen = pd.umd.traverse_lane_segments(
        umd_map=umd_map,
        start_lane_segment_id=start_lane_segment_id,
        traversal_strategy=lambda prev, successors: successors[0]
    )
    for lane_segment in lane_segments_gen:
        # Determine geometry for the lane
        ref_line = umd_map.edges.get(lane_segment.reference_line)
        lane_points = [(p.x, p.y, p.z) for p in ref_line.points]
        if lane_segment.direction == pd.umd.schema.LaneSegment.Direction.BACKWARD:
            lane_points = reversed(lane_points)
        # Add points to lane, exit when we hit boundaries
        for lane_point in lane_points:
            route_points.append(lane_point)
    return route_points


class SimVehicle:
    """
    Represents a vehicle in a simulation.

    This vehicle follows a route at a constant velocity
    """
    def __init__(self,
                 route_points: List[Tuple[float, float, float]],
                 speed_metres_per_sec: float,
                 wheel_radius_metres: float,
                 start_offset_metres: float):
        self.__poses = pd.umd.move_along_path(
            path_points=route_points,
            start_offset_metres=start_offset_metres,
        )
        self.__speed_metres = speed_metres_per_sec
        self.__wheel_angular_velocity_rad_per_sec = speed_metres_per_sec / wheel_radius_metres
        self.velocity = (0.0, 0.0, 0.0)
        self.pose = next(self.__poses)
        self.wheel_angle_radians = 0.0

    def step(self, time_delta_sec: float) -> bool:
        """
        Advance the state of the vehicle

        Args:
            time_delta_sec: Time step in seconds

        Returns:
            True if agent advanced, False if the route is complete
        """
        try:
            prev_pose = self.pose
            self.pose = self.__poses.send(self.__speed_metres*time_delta_sec)
            self.velocity = get_velocity(prev_pose, self.pose, time_delta_sec)
            self.wheel_angle_radians += self.__wheel_angular_velocity_rad_per_sec * time_delta_sec
        except StopIteration:
            return False
        return True


class VehicleAgentAdapter:
    """
    Represents a complete vehicle agent to be simulated and rendered

    Provides simulation state for a vehicle.
    Provides method to generate a complete pd.state.VehicleAgent
    """
    def __init__(self,
                 id: int,
                 vehicle_type: Optional[str],
                 route: List[Tuple[float, float, float]],
                 speed_metres_per_sec: float,
                 start_offset_metres: float,
                 **kwargs):
        self.id = id
        self.vehicle_type = vehicle_type
        self.wheel_type, self.wheel_poses, self.wheel_radius = None, None, 1.0
        self.kwargs = kwargs
        if vehicle_type:
            vehicle_wheels = get_vehicle_wheel_names(self.vehicle_type)
            if vehicle_wheels:
                self.wheel_type = vehicle_wheels[0]
                self.wheel_poses = get_vehicle_wheel_poses(self.vehicle_type, self.wheel_type)
                self.wheel_radius = get_wheel_radius(self.wheel_type)

        self.sim_agent = SimVehicle(
            route_points=route,
            wheel_radius_metres=self.wheel_radius,
            speed_metres_per_sec=speed_metres_per_sec,
            start_offset_metres=start_offset_metres
        )

    def generate_vehicle_agent(self) -> pd.state.VehicleAgent:
        if self.vehicle_type and self.wheel_poses:
            rotation = pd.state.Pose6D.from_euler_angles(
                x_metres=0.0, y_metres=0.0, z_metres=0.0,
                alpha_radians=-self.sim_agent.wheel_angle_radians, beta_radians=0.0, gamma_radians=0.0
            )
            wheel_poses_rotated = [
                p*rotation for p in self.wheel_poses
            ]
        else:
            wheel_poses_rotated = None
        vehicle_color = self.kwargs.get('vehicle_color', None)
        return pd.state.VehicleAgent(
            id=self.id,
            pose=self.sim_agent.pose,
            velocity=self.sim_agent.velocity,
            vehicle_type=self.vehicle_type,
            vehicle_color=vehicle_color,
            wheel_type=self.wheel_type,
            wheel_poses=wheel_poses_rotated,
            lock_to_ground=True
        )


@click.command()
@common_step_options(require_asset_registry=True, require_umd_path=True)
@click.option('--preview/--no-preview', default=True, show_default=True, help="Preview rendered frame")
@click.option('--sensor', help="Path to custom sensor rig. By default, uses the Barebones sensor rig")
@click.option(
    '-o', '--output-dir',
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
    default='./output',
    help="Output directory for images",
    show_default=True
)
@click.option('-f', '--force', help="Force overwrite output", is_flag=True, default=False)
@click.option('-d', '--debug', is_flag=True, help="Output debug logs")
def cli(preview, sensor, output_dir, force, debug, step_options: StepScriptContext = None):
    """
    Highway Traffic Step Mode scenario

    This example simulates a number of vehicles driving on a highway.
    It demonstrates how to use the UMD map to locate roads and create trajectories for an agent.
    It also demonstrates how to send State information to and retrieve simulator sensor data from
    a Step server.
    """
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        level=logging.DEBUG if debug else logging.INFO,
                        stream=sys.stdout)

    request_addr = step_options.ig
    client_cert_file = step_options.client_cert_file

    level_name, level_version = DEFAULT_LOCATION
    lighting = DEFAULT_LIGHTING

    # Set up output directory
    output_path = Path(output_dir)
    if output_path.exists():
        if force:
            shutil.rmtree(output_path)
        else:
            sys.exit(f"Error: Output directory {output_path} already exists. Please specify a different directory.")
    output_path.mkdir(exist_ok=True)
    rgb_output_path = output_path / "rgb"
    depth_output_path = output_path / "depth"
    semseg_output_path = output_path / "semantic_segmentation_2d"
    instance_output_path = output_path / "instance_segmentation_2d"

    # Load route information
    if step_options.internal_dev:
        umd_map = pd.umd.load_umd_map_from_file(step_options.umd_path)
    else:
        umd_map = pd.umd.load_umd_map(level_name, level_version)

    # Load sensor rig
    sensor_list = pd.state.load_sensor_rig(sensor if sensor else pd.state.SensorRig.BAREBONES_ALL)

    click.echo("Connecting to server...", nl=False)
    session = pd.session.StepSession(request_addr=request_addr, client_cert_file=client_cert_file)
    with session:
        click.echo("done.")
        version = session.system_info.version
        click.echo(f"Server version: {version.major}.{version.minor}.{version.patch}-{version.build}")
        click.echo(f"Loading map {level_name}...", nl=False)
        session.load_location(level_name, lighting)
        click.echo("done")

        route_ego = generate_route(umd_map=umd_map, start_lane_segment_id=116)
        route_lane_1 = generate_route(umd_map=umd_map, start_lane_segment_id=116)
        route_lane_2 = generate_route(umd_map=umd_map, start_lane_segment_id=117)

        vehicle_ego = VehicleAgentAdapter(
            id=pd.state.rand_agent_id(),
            vehicle_type=None,
            route=route_ego,
            speed_metres_per_sec=20.0,
            start_offset_metres=0.0
        )

        other_vehicles = [
            VehicleAgentAdapter(
                id=pd.state.rand_agent_id(),
                vehicle_type='compact_sport_01',
                route=route_lane_2,
                speed_metres_per_sec=17.0,
                start_offset_metres=20.0,
                vehicle_color='silver'
            ),
            VehicleAgentAdapter(
                id=pd.state.rand_agent_id(),
                vehicle_type='midsize_sedan_04',
                route=route_lane_2,
                speed_metres_per_sec=17.0,
                start_offset_metres=40.0,
            ),
            VehicleAgentAdapter(
                id=pd.state.rand_agent_id(),
                vehicle_type='compact_sport_02',
                route=route_lane_2,
                speed_metres_per_sec=17.0,
                start_offset_metres=50.0,
            ),
            VehicleAgentAdapter(
                id=pd.state.rand_agent_id(),
                vehicle_type='suv_medium_02',
                route=route_lane_2,
                speed_metres_per_sec=17.0,
                start_offset_metres=64.0,
            ),
            VehicleAgentAdapter(
                id=pd.state.rand_agent_id(),
                vehicle_type='truck_cement_mixer_01',
                route=route_lane_2,
                speed_metres_per_sec=17.0,
                start_offset_metres=80.0,
            ),
            VehicleAgentAdapter(
                id=pd.state.rand_agent_id(),
                vehicle_type='midsize_muscle_01',
                route=route_lane_1,
                speed_metres_per_sec=23.0,
                start_offset_metres=7.0,
            ),
        ]

        # Initialize simulation state
        time_delta_sec = 1.0 / float(SIM_RATE_PER_SECOND)
        frame_count = 0
        time_sec = 0.0

        # Main loop
        while time_sec < MAX_SIM_TIME_SEC:
            do_render_frame = frame_count % RENDER_FRAME_INTERVAL == 0
            do_capture_frame = frame_count % (RENDER_FRAME_INTERVAL * CAPTURE_FRAME_INTERVAL) == 0
            click.echo(f"Frame {frame_count}, Time {time_sec:.3f}s, Render {do_render_frame}, Capture {do_capture_frame}")

            world_info = pd.state.WorldInfo()

            agent_ego = vehicle_ego.generate_vehicle_agent()
            agent_ego.sensors = sensor_list
            agents = [agent_ego] + [v.generate_vehicle_agent() for v in other_vehicles]
            state = pd.state.State(
                simulation_time_sec=time_sec,
                world_info=world_info,
                agents=agents
            )

            if do_render_frame:
                # Send state to server
                session.update_state(state)

            if do_capture_frame:
                # Loop over all the sensors
                preview_rgb_image = None
                for sensor in sensor_list:
                    if not isinstance(sensor, pd.state.sensor.CameraSensor):
                        continue

                    # Query RGB data
                    sensor_data = session.query_sensor_data(agent_ego.id, sensor.name, pd.state.SensorBuffer.RGB)
                    if not (sensor_data.height > 0 and sensor_data.width > 0):
                        sys.exit("Error: Failed to query RGB data from IG")
                    rgb_image = sensor_data.data_as_rgb
                    save_image(rgb_output_path, sensor.name, frame_count,
                               cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR))
                    preview_rgb_image = rgb_image if preview_rgb_image is None else preview_rgb_image  # save for preview

                    # Query depth data
                    if sensor.capture_depth:
                        try:
                            sensor_data = session.query_sensor_data(agent_ego.id, sensor.name, pd.state.SensorBuffer.DEPTH)
                            depth_data = sensor_data.data_as_depth
                            depth_image = depth_data.astype(np.uint8)
                            save_image(depth_output_path, sensor.name, frame_count,
                                       cv2.applyColorMap(depth_image, cv2.COLORMAP_JET))
                        except PdError:
                            pass

                    # Query semantic segmentation data
                    if sensor.capture_segmentation:
                        try:
                            sensor_data = session.query_sensor_data(agent_ego.id, sensor.name, pd.state.SensorBuffer.SEGMENTATION)
                            semseg_image = sensor_data.data_as_segmentation_rgb
                            save_image(semseg_output_path, sensor.name, frame_count,
                                       cv2.cvtColor(semseg_image, cv2.COLOR_RGB2BGR))
                        except PdError:
                            pass

                    # Query instance segmentation data
                    if sensor.capture_instances:
                        try:
                            sensor_data = session.query_sensor_data(agent_ego.id, sensor.name, pd.state.SensorBuffer.INSTANCES)
                            instance_image = sensor_data.get_data_as_merged_instance_rgb(rgb_image)
                            save_image(instance_output_path, sensor.name, frame_count,
                                       cv2.cvtColor(instance_image, cv2.COLOR_RGB2BGR))
                        except PdError:
                            pass

                if preview:
                    try:
                        cv2.imshow('img', cv2.cvtColor(preview_rgb_image, cv2.COLOR_RGB2BGR))
                        key = cv2.waitKey(1)
                        # Escape key to exit program
                        if key == 27:
                            return
                    except cv2.error:
                        click.echo(f"Couldn't display GUI window, skipping preview")

            # Advance the simulation state
            frame_count += 1
            time_sec += time_delta_sec
            if not vehicle_ego.sim_agent.step(time_delta_sec):
                break
            for vehicle in other_vehicles:
                vehicle.sim_agent.step(time_delta_sec)


if __name__ == '__main__':
    cli()
