# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import click
import sys
from typing import List, Tuple
import random
from pathlib import Path

import numpy as np
import cv2

import pd.session
import pd.state
import pd.umd
from pd.core import PdError
from pd.util.scripting import common_step_options, StepScriptContext


DEFAULT_LOCATION = ('SF_6thAndMission_medium', 'v2.0.1')
DEFAULT_LIGHTING = 'LS_sky_noon_partlyCloudy_1113_HDS024'
SIM_RATE_PER_SECOND = 100  # Our simulation runs at this rate
MAX_SIM_TIME_SEC = 25.0
MAX_SIM_DISTANCE_METRES = 1000

# Render interval controls render frame rate. Lower render interval yields higher fidelity camera data.
# Simulation rate is typically 100fps. RENDER_INTERVAL=1 will yield a render frame rate of 100fps.
# RENDER_INTERVAL=10 will yield a render frame rate of 10fps.
#
# Capture interval controls the frame rate of output data. Lower capture interval yields higher output frame rate.
# Given a render frame rate of 100fps, CAPTURE_INTERVAL=10 will yield an output frame rate of 10fps.
#
# Default values of RENDER_INTERVAL=1, CAPTURE_INTERVAL=10 yield render rate of 100fps and output frame rate of 10fps.
RENDER_FRAME_INTERVAL = 1  # Every Nth simulation state is rendered
CAPTURE_FRAME_INTERVAL = 10  # Every Nth render is saved/displayed


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


def generate_route(umd_map) -> List[Tuple[float, float, float]]:
    """
    Generates a random route spanning driveable lane segments
    Args:
        umd_map:

    Returns:
        Generated route as a list of points
    """
    # Let's start by randomly selecting a road
    valid_road_types = {
        pd.umd.schema.RoadSegment.RoadType.MOTORWAY,
        pd.umd.schema.RoadSegment.RoadType.TRUNK,
        pd.umd.schema.RoadSegment.RoadType.PRIMARY,
        pd.umd.schema.RoadSegment.RoadType.SECONDARY,
        pd.umd.schema.RoadSegment.RoadType.RESIDENTIAL,
        pd.umd.schema.RoadSegment.RoadType.MOTORWAY_LINK,
    }
    # Filter for valid road types
    roads = filter(lambda r: r.type in valid_road_types, umd_map.road_segments.values())
    # Filter for roads with at least one driveable lane
    roads = filter(
        lambda r: any(umd_map.lane_segments.get(lane_id).type == pd.umd.schema.LaneSegment.LaneType.DRIVABLE
                      for lane_id in r.lane_segments),
        roads
    )
    roads = sorted(roads, key=lambda r: r.id)  # sort for determinism
    selected_road = random.choice(roads)

    # Randomly select a starting lane segment
    lane_segments = (umd_map.lane_segments.get(lane_id) for lane_id in selected_road.lane_segments)
    lane_segments = filter(lambda l: l.type == pd.umd.schema.LaneSegment.LaneType.DRIVABLE, lane_segments)
    selected_lane_segment = random.choice(list(lane_segments))

    # Traverse lane segments, selecting a random successor each time, to generate a path of points
    route_points = []
    lane_segments_gen = pd.umd.traverse_lane_segments(
        umd_map=umd_map,
        start_lane_segment_id=selected_lane_segment.id,
        traversal_strategy=lambda prev, successors: random.choice(successors)
    )
    total_distance_traversed_in_metres = 0.0
    for lane_segment in lane_segments_gen:
        ref_line = umd_map.edges.get(lane_segment.reference_line)
        total_distance_traversed_in_metres += pd.umd.get_edge_length_in_metres(ref_line)
        lane_points = [(p.x, p.y, p.z) for p in ref_line.points]
        if lane_segment.direction == pd.umd.schema.LaneSegment.Direction.BACKWARD:
            lane_points = reversed(lane_points)
        route_points += lane_points
        if total_distance_traversed_in_metres > MAX_SIM_DISTANCE_METRES:
            break

    return route_points


@click.command()
@common_step_options()
@click.option('--preview/--no-preview', default=True, show_default=True, help="Preview rendered frame")
@click.option('--location', default=DEFAULT_LOCATION, help="Location name and version", type=(str, str),
              show_default=True)
@click.option('--lighting', default=DEFAULT_LIGHTING, help="Name of lightning level", show_default=True)
@click.option('--streetlights', is_flag=True, help="Enable streetlights", show_default=True)
@click.option('--sensor', help="Path to custom sensor rig. By default, uses the Barebones sensor rig")
@click.option('--seed', default=0, type=int, help="Seed to randomize the route", show_default=True)
@click.option(
    '-o', '--output-dir',
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
    default='./output',
    help="Output directory for images",
    show_default=True
)
def cli(preview, location, lighting, streetlights, sensor, seed, output_dir, step_options: StepScriptContext = None):
    """
    Hello World Step Mode example

    This example simulates an ego agent driving in an empty world.
    It demonstrates how to use the UMD map to locate roads and create trajectories for an agent.
    It also demonstrates how to send State information to and retrieve simulator sensor data from
    a Step server.
    """
    request_addr = step_options.ig
    client_cert_file = step_options.client_cert_file

    random.seed(seed)

    # Set up output directory
    output_path = Path(output_dir)
    if output_path.exists():
        sys.exit(f"Error: Output directory {output_path} already exists. Please specify a different directory.")
    rgb_output_path = output_path / "rgb"
    depth_output_path = output_path / "depth"
    semseg_output_path = output_path / "semantic_segmentation_2d"
    instance_output_path = output_path / "instance_segmentation_2d"
    normals_2d_output_path = output_path / "surface_normals_2d"

    # Load route information
    level_name, level_version = location
    umd_map = step_options.load_umd_map(level_name, level_version)
    ego_route_points = generate_route(umd_map=umd_map)
    # Set up generator for pose calculation
    ego_poses = pd.umd.move_along_path(
        path_points=ego_route_points,
        start_offset_metres=0.0,
    )

    # Load sensor rig
    sensor_list = pd.state.load_sensor_rig(sensor if sensor else pd.state.SensorRig.DEMO_RIG_SIMPLE_FRONT_ALL)

    click.echo("Connecting to server...", nl=False)
    session = pd.session.StepSession(request_addr=request_addr, client_cert_file=client_cert_file)
    with session:
        click.echo("done.")
        version = session.system_info.version
        click.echo(f"Server version: {version.major}.{version.minor}.{version.patch}-{version.build}")
        click.echo(f"Loading map {level_name}...", nl=False)
        session.load_location(level_name, lighting)
        click.echo("done")

        # Initialize simulation state
        time_delta_sec = 1.0 / float(SIM_RATE_PER_SECOND)
        frame_count = 0
        time_sec = 0.0
        ego_pose = next(ego_poses)
        ego_velocity = (0.0, 0.0, 0.0)
        ego_agent_id = pd.state.rand_agent_id()

        # Main loop
        while time_sec < MAX_SIM_TIME_SEC:
            do_render_frame = frame_count % RENDER_FRAME_INTERVAL == 0
            do_capture_frame = frame_count % (RENDER_FRAME_INTERVAL * CAPTURE_FRAME_INTERVAL) == 0
            click.echo(f"Frame {frame_count}, Time {time_sec:.3f}s, Render {do_render_frame}, Capture {do_capture_frame}")

            # Create state for current frame
            ego_agent = pd.state.SensorAgent(
                id=ego_agent_id,
                pose=ego_pose,
                velocity=ego_velocity,
                sensors=sensor_list
            )
            world_info = pd.state.WorldInfo(
                street_lights=streetlights
            )

            state = pd.state.State(
                simulation_time_sec=time_sec,
                world_info=world_info,
                agents=[ego_agent]
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
                    try:
                        sensor_data = session.query_sensor_data(ego_agent.id, sensor.name, pd.state.SensorBuffer.RGB)
                    except PdError:
                        sys.exit("Error: Failed to query RGB data from IG")
                    rgb_image = sensor_data.data_as_rgb
                    save_image(rgb_output_path, sensor.name, frame_count,
                               cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR))
                    preview_rgb_image = rgb_image if preview_rgb_image is None else preview_rgb_image  # save for preview

                    # Query depth data
                    if sensor.capture_depth:
                        try:
                            sensor_data = session.query_sensor_data(ego_agent.id, sensor.name, pd.state.SensorBuffer.DEPTH)
                            depth_data = sensor_data.data_as_depth
                            depth_image = depth_data.astype(np.uint8)
                            save_image(depth_output_path, sensor.name, frame_count,
                                       cv2.applyColorMap(depth_image, cv2.COLORMAP_JET))
                        except PdError:
                            pass

                    # Query semantic segmentation data
                    if sensor.capture_segmentation:
                        try:
                            sensor_data = session.query_sensor_data(ego_agent.id, sensor.name, pd.state.SensorBuffer.SEGMENTATION)
                            semseg_image = sensor_data.data_as_segmentation_rgb
                            save_image(semseg_output_path, sensor.name, frame_count,
                                       cv2.cvtColor(semseg_image, cv2.COLOR_RGB2BGR))
                        except PdError:
                            pass

                    # Query instance segmentation data
                    if sensor.capture_instances:
                        try:
                            sensor_data = session.query_sensor_data(ego_agent.id, sensor.name, pd.state.SensorBuffer.INSTANCES)
                            instance_image = sensor_data.get_data_as_merged_instance_rgb(rgb_image)
                            save_image(instance_output_path, sensor.name, frame_count,
                                       cv2.cvtColor(instance_image, cv2.COLOR_RGB2BGR))
                        except PdError:
                            pass

                    # Query normals data
                    if sensor.capture_normals:
                        try:
                            sensor_data = session.query_sensor_data(ego_agent.id, sensor.name, pd.state.SensorBuffer.NORMALS)
                            normals_2d_image = sensor_data.data_as_rgb
                            save_image(normals_2d_output_path, sensor.name, frame_count,
                                       cv2.cvtColor(normals_2d_image, cv2.COLOR_RGB2BGR))
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

            frame_count += 1
            time_sec += time_delta_sec
            ego_speed = 30.0
            try:
                ego_prev_pose = ego_pose
                ego_pose = ego_poses.send(ego_speed*time_delta_sec)
                ego_velocity = get_velocity(ego_prev_pose, ego_pose, time_delta_sec)
            except StopIteration:
                break


if __name__ == '__main__':
    cli()
