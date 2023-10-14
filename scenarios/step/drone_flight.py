# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import logging
import shutil
import sys
from pathlib import Path
from typing import Tuple

import click
import cv2
import numpy as np

import pd.management
import pd.session
import pd.state
import pd.umd
from pd.util import StepScriptContext, common_step_options

DEFAULT_LOCATION = ("SJ_EssexAndBradford", "v2.0.2")
LIGHTING_CHOICES = {"day": "LS_sky_noon_mostlySunny_1250_HDS025", "night": "LS_sky_twilight_clear_0400_HDS023"}


START_HEIGHT_METRES = 60.0
END_HEIGHT_METRES = 10.0
DESCENT_VELOCITY_METRES_PER_SEC = 30.0
SIM_STEP_INTERVAL_SEC = 0.1
OFFSET_X = 1.0
OFFSET_Y = 0.0


def save_image(base_path: Path, sensor_name: str, frame: int, image):
    """
    Save cv2 image to disk
    Args:
        base_path: Base output directory path
        agent_id: Agent id
        sensor_name: Name of sensor
        frame: Frame number
        image: CV2 image to save
    """
    image_path = base_path / f"{sensor_name}" / f"{frame:06d}.png"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    click.echo(f"Saving image: {image_path}")
    cv2.imwrite(str(image_path), image)


def get_starting_position_from_umd(umd_map, seed: int):
    """
    Extracts a starting position from the UMD spec

    This method finds a driveway in the UMD and returns its location.

    Args:
        umd_map: Umd map

    Returns:
        Location 3-tuple
    """
    # Find all the driveways
    driveways = [
        road for road in umd_map.road_segments.values() if road.type == pd.umd.schema.RoadSegment.RoadType.DRIVEWAY
    ]
    driveways = sorted(driveways, key=lambda d: d.id)
    # Select the first driveway
    driveway = driveways[seed % len(driveways)]
    lane_id = driveway.lane_segments[0]
    lane_segment = umd_map.lane_segments.get(lane_id)
    ref_line = umd_map.edges.get(lane_segment.reference_line)
    starting_point = ref_line.points[0]
    return starting_point.x, starting_point.y, starting_point.z


class DroneSimulator:
    """
    Super simple drone simulatior

    Simulates a descending drone given a starting position and target height.
    """

    def __init__(
        self,
        start_pos_metres: Tuple[float, float, float],
        target_height_metres: float,
        descent_velocity_metres_per_sec: float,
        step_interval_sec: float,
    ):
        self.world_time = 0.0
        self.current_pos_metres = start_pos_metres
        self._target_height_metres = target_height_metres
        self._descent_velocity_metres_per_sec = descent_velocity_metres_per_sec
        self._step_interval_sec = step_interval_sec

    def step(self) -> bool:
        """
        Advance simulation state by one step

        Returns:
            True if simulation advanced, False if simulation has ended
        """
        x, y, z = self.current_pos_metres
        if z <= self._target_height_metres:
            return False
        z -= self._descent_velocity_metres_per_sec * self._step_interval_sec
        self.current_pos_metres = (x, y, z)
        self.world_time += self._step_interval_sec
        return True


@click.command()
@common_step_options()
@click.option("--preview/--no-preview", default=True, show_default=True, help="Preview rendered frame")
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
    default="./output",
    help="Output directory for images",
    show_default=True,
)
@click.option(
    "--location", default=DEFAULT_LOCATION, help="Location name and version", type=(str, str), show_default=True
)
@click.option("--day/--night", help="Time of day", default=True)
@click.option("--grayscale", help="Grayscale camera sensor", is_flag=True, default=False)
@click.option("--seed", default=0, type=int, help="Seed to randomize the starting location", show_default=True)
@click.option("-f", "--force", help="Force overwrite output", is_flag=True, default=False)
def cli(preview, output_dir, location, day, grayscale, seed, force, step_options: StepScriptContext = None):
    """
    Drone flight Step Mode example

    This step mode example simulates a drone landing on a residential driveway.
    It illustrates how to connect to and communicate with a server.
    It also shows how the UMD specification can be used to extract location information.
    """
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO, stream=sys.stdout)

    request_addr = step_options.ig
    client_cert_file = step_options.client_cert_file

    output_path = Path(output_dir)
    if output_path.exists():
        if force:
            shutil.rmtree(output_path)
        else:
            sys.exit(f"Error: Output directory {output_path} already exists. Please specify a different directory.")
    output_path.mkdir(exist_ok=True)

    lighting = LIGHTING_CHOICES["day"] if day else LIGHTING_CHOICES["night"]

    level_name, level_version = location
    umd_map = step_options.load_umd_map(level_name, level_version)
    start_x, start_y, start_z = get_starting_position_from_umd(umd_map, seed)
    ego_agent_id = pd.state.rand_agent_id()

    click.echo("Connecting to server...", nl=False)
    session = pd.session.StepSession(request_addr=request_addr, client_cert_file=client_cert_file)
    with session:
        click.echo("done.")
        version = session.system_info.version
        click.echo(f"Server version: {version.major}.{version.minor}.{version.patch}-{version.build}")
        click.echo(f"Loading map {level_name}...", nl=False)
        session.load_location(level_name, lighting)
        click.echo("done")

        sim = DroneSimulator(
            start_pos_metres=(start_x + OFFSET_X, start_y + OFFSET_Y, start_z + START_HEIGHT_METRES),
            target_height_metres=start_z + END_HEIGHT_METRES,
            descent_velocity_metres_per_sec=DESCENT_VELOCITY_METRES_PER_SEC,
            step_interval_sec=SIM_STEP_INTERVAL_SEC,
        )

        frame_count = 0
        while sim.step():
            x, y, z = sim.current_pos_metres
            click.echo(f"Frame {frame_count} (height={z-start_z} metres)")

            sensor = pd.state.CameraSensor(
                name="Front",
                pose=pd.state.Pose6D.from_rpy_angles(
                    x_metres=0.0, y_metres=0.0, z_metres=0.0, roll_degrees=0.0, pitch_degrees=0.0, yaw_degrees=0.0
                ),
                width=1920,
                height=1080,
                field_of_view_degrees=90,
                capture_rgb=True,
                capture_segmentation=True,
                capture_depth=True,
                capture_instances=True,
                post_process_params=pd.state.PostProcessParams(
                    motion_blur_amount=0.5,
                ),
                transmit_gray=grayscale,
            )
            lidar = pd.state.LiDARSensor(
                name="Altitude",
                pose=pd.state.Pose6D.from_rpy_angles(
                    x_metres=0.0, y_metres=0.0, z_metres=0.0, roll_degrees=0.0, pitch_degrees=0.0, yaw_degrees=0.0
                ),
                sample_rate=10.0,
                rotation_rate=1.0,
                beam_data=[pd.state.LiDARBeam(0, 0.0, 0.0)],
            )
            sensor_agent = pd.state.ModelAgent(
                id=ego_agent_id,
                pose=pd.state.Pose6D.from_rpy_angles(
                    x_metres=x, y_metres=y, z_metres=z, roll_degrees=0.0, pitch_degrees=-90.0, yaw_degrees=0.0
                ),
                velocity=(0.0, 0.0, 0.0),
                asset_name="spotlight_01",
                sensors=[sensor, lidar],
            )
            world_info = pd.state.WorldInfo(street_lights=1.0)

            state = pd.state.State(simulation_time_sec=sim.world_time, world_info=world_info, agents=[sensor_agent])

            # Send the environment state to server
            session.update_state(state)

            # Request LiDAR data from the server
            lidar_data = session.query_sensor_data(sensor_agent.id, lidar.name, pd.state.SensorBuffer.RGB)
            measured_altitude = lidar_data.data[0][2]
            click.echo(f"Altitude measured with LiDAR: {measured_altitude:.2f} metres")

            # Query camera sensor data
            sensor_data = session.query_sensor_data(sensor_agent.id, sensor.name, pd.state.SensorBuffer.RGB)
            rgb_data = sensor_data.data_as_rgb
            save_image(output_path, "rgb", frame_count, cv2.cvtColor(rgb_data, cv2.COLOR_RGB2BGR))

            # Query depth annotation data
            sensor_data = session.query_sensor_data(sensor_agent.id, sensor.name, pd.state.SensorBuffer.DEPTH)
            depth_data = sensor_data.data_as_depth
            center_pixel_depth = depth_data[tuple(np.array(depth_data.shape) // 2)]
            depth_image = depth_data.astype(np.uint8)  # convert to uint8
            save_image(output_path, "depth", frame_count, cv2.applyColorMap(depth_image, cv2.COLORMAP_JET))
            click.echo(f"Center pixel depth: {center_pixel_depth:.2f}")

            # Query semantic segmentation annotation data
            sensor_data = session.query_sensor_data(sensor_agent.id, sensor.name, pd.state.SensorBuffer.SEGMENTATION)
            semseg_image = sensor_data.data_as_segmentation_rgb
            semseg_labels = sensor_data.data_as_segmentation_labels
            save_image(output_path, "semseg", frame_count, semseg_image)
            click.echo(f"Semantic labels in scene: {', '.join(np.unique(semseg_labels))}")

            # Query instance segmentation annotation data
            sensor_data = session.query_sensor_data(sensor_agent.id, sensor.name, pd.state.SensorBuffer.INSTANCES)
            instances_image = sensor_data.get_data_as_merged_instance_rgb(rgb_data)
            instances_data = sensor_data.data_as_instance_ids
            save_image(output_path, "instances", frame_count, cv2.cvtColor(instances_image, cv2.COLOR_RGB2BGR))
            click.echo(f"Instance ids in scene: {', '.join(map(str, np.unique(instances_data)))}")

            if preview:
                try:
                    cv2.imshow("img", cv2.cvtColor(rgb_data, cv2.COLOR_RGB2BGR))
                    key = cv2.waitKey(1)
                    # Escape key to exit program
                    if key == 27:
                        return
                except cv2.error:
                    click.echo("Couldn't display GUI window, skipping preview")

            frame_count += 1
            click.echo("----------------------------------------")


if __name__ == "__main__":
    cli()
