# Copyright (c) 2022 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import random
import sys
from pathlib import Path
import logging
import shutil
import json

import click
import cv2

from pd.session import StepSession
from pd.state import (
    Pose6D, SensorAgent, VehicleAgent, ModelAgent, WorldInfo, State, rand_agent_id,
    sensors_from_json, SensorBuffer
)
from pd.assets import (
    ObjAssets, get_category_names, get_asset_names_in_category,
    get_vehicle_wheel_names, get_vehicle_wheel_poses
)
from pd.util import common_step_options, StepScriptContext
from pd.umd import load_default_umd_map, get_nearest_point_to


logger = logging.getLogger(__name__)

_DEFAULT_SENSOR_RIG = """
{
    "sensor_configs": [
        {
            "display_name": "simple_camera",
            "camera_intrinsic": {
                "width": 1280,
                "height": 720,
                "fov": 50,
                "capture_rgb": true,
                "capture_segmentation": true,
                "post_process_params": {
                    "motion_blur_amount": 0.0
                }
            },
            "sensor_extrinsic": {
                "yaw": 0.0,
                "pitch": 0.0,
                "roll": 0.0,
                "x": 0.0,
                "y": 0.0,
                "z": 0.0
            }
        }
    ]
}
"""

# Render additional substeps before capturing to increase quality
_RENDER_SUBSTEPS = 5

# World coordinates where asset is placed
ASSET_X_OFFSET, ASSET_Y_OFFSET = 0, -5


def save_image(base_path: Path, asset_name: str, rotation: int, image):
    image_path = base_path / f"{asset_name}-{rotation:03d}.png"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(image_path), image)
    logger.info(f"Saving image: {image_path}")


@click.command()
@common_step_options()
@click.option(
    '-o', '--output',
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
    default='./output',
    help="Output directory for images",
    show_default=True
)
@click.option('-f', '--force', help="Force overwrite output", is_flag=True, default=False)
def cli(output, force, step_options: StepScriptContext = None):
    """
    Asset Viewpoints example

    This example demonstrates how to capture different viewpoints of a single asset.
    """
    random.seed(1)
    logging.basicConfig(format='',
                        level=logging.INFO,
                        stream=sys.stdout)

    request_addr = step_options.ig
    client_cert_file = step_options.client_cert_file

    # Set up output directory
    output_path = Path(output)
    if output_path.exists():
        if force:
            shutil.rmtree(output_path)
        else:
            sys.exit(f"Error: Output directory {output_path} already exists. Please specify a different directory.")
    output_path.mkdir(exist_ok=True)
    rgb_output_path = output_path / "rgb"
    semseg_output_path = output_path / "semantic_segmentation_2d"

    # Create sensor rig object
    default_sensor_rig = sensors_from_json(json.loads(_DEFAULT_SENSOR_RIG))

    logger.info("Available categories: " + ", ".join(get_category_names()))

    # Let's select a couple of assets
    vehicle_names = list(get_asset_names_in_category('vehicle'))
    bench_names = list(filter(lambda n: 'bench' in n, get_asset_names_in_category('prop')))
    asset_names = [
        random.choice(vehicle_names),  # a random vehicle
        random.choice(bench_names),  # a random bench
    ]
    logger.info("Selected asset names: " + ", ".join(asset_names))

    umd_map = load_default_umd_map()
    nearest_position = get_nearest_point_to(umd_map, 0, 0)
    ground_z = nearest_position[2]

    world_time = 0.0
    session = StepSession(request_addr=request_addr, client_cert_file=client_cert_file)
    logger.info("Connecting to server...")
    with session:
        logger.info("done.")
        version = session.system_info.version
        logger.info(f"Server version: {version.major}.{version.minor}.{version.patch}-{version.build}")
        logger.info("Loading map...")
        session.load_default_location()
        logger.info("done")

        # Let's loop through our selected assets
        for asset_name in asset_names:

            asset_obj = ObjAssets.get_or_none(ObjAssets.name == asset_name)
            if not asset_obj:
                sys.exit(f"Failed to find asset '{asset_name}'")
            category_name = asset_obj.asset_category.name if asset_obj.asset_category and asset_obj.asset_category.name \
                else 'none'

            asset_pose = Pose6D.from_rpy_angles(
                x_metres=ASSET_X_OFFSET, y_metres=ASSET_Y_OFFSET, z_metres=ground_z,
                roll_degrees=0.0, pitch_degrees=0.0, yaw_degrees=90.0
            )
            camera_pose = Pose6D.from_rpy_angles(
                x_metres=ASSET_X_OFFSET+10.0, y_metres=ASSET_Y_OFFSET+10.0, z_metres=ground_z+1.5,
                roll_degrees=0, pitch_degrees=0, yaw_degrees=135.0
            )
            sensor_agent = SensorAgent(
                id=rand_agent_id(),
                pose=camera_pose,
                velocity=(0.0, 0.0, 0.0),
                sensors=default_sensor_rig
            )

            if category_name == 'vehicle':
                vehicle_agent = VehicleAgent(
                    id=rand_agent_id(),
                    pose=asset_pose,
                    velocity=(0, 0, 0),
                    vehicle_type=asset_obj.name,
                )
                vehicle_name = asset_obj.name
                vehicle_wheels = get_vehicle_wheel_names(vehicle_name)
                wheel_name = vehicle_wheels[0] if vehicle_wheels else None
                wheel_poses = get_vehicle_wheel_poses(vehicle_name, wheel_name) if vehicle_wheels else []
                vehicle_agent.wheel_type = wheel_name
                vehicle_agent.wheel_poses = wheel_poses
                agent = vehicle_agent
            else:
                model_agent = ModelAgent(
                    id=rand_agent_id(),
                    pose=asset_pose,
                    velocity=(0.0, 0.0, 0.0),
                    asset_name=asset_obj.name,
                )
                agent = model_agent

            world_info = WorldInfo()

            state = State(
                simulation_time_sec=world_time,
                world_info=world_info,
                agents=[sensor_agent, agent]
            )

            # Warm up the render to clean up any ghosting from previous asset
            for _ in range(_RENDER_SUBSTEPS):
                session.update_state(state)
                state.simulation_time_sec += 0.01

            # Let's rotate the asset in small increments
            for rotation in range(0, 360, 10):
                # Apply the rotation
                agent.pose = asset_pose * Pose6D.from_rpy_angles(
                    0, 0, 0,
                    roll_degrees=0, pitch_degrees=0, yaw_degrees=rotation
                )

                # Render state by sending messages to server
                for _ in range(_RENDER_SUBSTEPS):
                    session.update_state(state)
                    world_time += 0.01
                    state.simulation_time_sec = world_time

                # Query sensor data from server and save images
                sensor_agent = next(a for a in state.agents if isinstance(a, SensorAgent))
                sensor_data = session.query_sensor_data(sensor_agent.id, sensor_agent.sensors[0].name, SensorBuffer.RGB)
                rgb_data = sensor_data.data_as_rgb
                save_image(rgb_output_path, asset_name, rotation, cv2.cvtColor(rgb_data, cv2.COLOR_RGB2BGR))
                sensor_data = session.query_sensor_data(sensor_agent.id, sensor_agent.sensors[0].name, SensorBuffer.SEGMENTATION)
                semseg_data = sensor_data.data_as_segmentation_rgb
                save_image(semseg_output_path, asset_name, rotation, cv2.cvtColor(semseg_data, cv2.COLOR_RGB2BGR))


if __name__ == '__main__':
    cli()
