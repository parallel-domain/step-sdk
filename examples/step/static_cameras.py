# Copyright (c) 2022 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import json
import logging
import math
import os
import shutil
import sys
from pathlib import Path

import click
import cv2
from matplotlib import pyplot as plt

import pd.session
import pd.state
from pd.util import StepScriptContext, common_step_options

_DEFAULT_SENSOR_RIG = """
{
    "sensor_configs": [
        {
            "display_name": "simple_camera",
            "camera_intrinsic": {
                "width": 1280,
                "height": 720,
                "fov": 50,
                "capture_rgb": true
            },
            "sensor_extrinsic": {
                "yaw": 0.0,
                "pitch": 0.0,
                "roll": 0.0,
                "x": 0.0,
                "y": 0.0,
                "z": 2.0
            }
        }
    ]
}
"""

# Render interval controls render frame rate. Lower render interval yields higher fidelity camera data.
# Simulation rate is typically 100fps. RENDER_INTERVAL=1 will yield a render frame rate of 100fps.
# RENDER_INTERVAL=10 will yield a render frame rate of 10fps.
#
# Capture interval controls the frame rate of output data. Lower capture interval yields higher output frame rate.
# Given a render frame rate of 100fps, CAPTURE_INTERVAL=10 will yield an output frame rate of 10fps.
#
# Default values of RENDER_INTERVAL=1, CAPTURE_INTERVAL=10 yield render rate of 100fps and output frame rate of 10fps.
_RENDER_INTERVAL = 1
_CAPTURE_INTERVAL = 10


def save_image(base_path: Path, agent_id: int, sensor_name: str, frame: int, image):
    """
    Save cv2 image to disk
    Args:
        base_path: Base output directory path
        agent_id: Agent id
        sensor_name: Name of sensor
        frame: Frame number
        image: CV2 image to save
    """
    image_path = base_path / f"agent{agent_id}-{sensor_name}" / f"{frame:06d}.png"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    click.echo(f"Saving image: {image_path}")
    cv2.imwrite(str(image_path), image)


@click.command()
@common_step_options()
@click.option("--preview/--no-preview", default=True, show_default=True, help="Preview rendered frame")
@click.option(
    "-i",
    "--input",
    type=click.Path(exists=True, file_okay=False),
    required=True,
    help="Path to directory with input State files. Must contain only '*.pd' files",
)
@click.option(
    "-o",
    "--output",
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
    default="./output",
    help="Output directory for images",
    show_default=True,
)
@click.option("-f", "--force", help="Force overwrite output", is_flag=True, default=False)
def cli(preview, input, output, force, step_options: StepScriptContext = None):
    """
    Static Cameras example

    This example demonstrates how to add static cameras to an existing scene and capture sensor data from
    those cameras.
    """
    # Hide warnings from deserializer
    logging.getLogger("pd.state.serialize").setLevel(logging.CRITICAL)

    request_addr = step_options.ig
    client_cert_file = step_options.client_cert_file

    # Validate input files
    input_path = Path(input)
    (_, _, filenames) = next(os.walk(input_path))
    if not filenames or any(not f.endswith(".pd") for f in filenames):
        sys.exit("Error: Input directory must contain only State files")
    filenames = sorted(filenames)

    # Set up output directory
    output_path = Path(output)
    if output_path.exists():
        if force:
            shutil.rmtree(output_path)
        else:
            sys.exit(f"Error: Output directory {output_path} already exists. Please specify a different directory.")
    output_path.mkdir(exist_ok=True)
    rgb_output_path = output_path / "rgb"

    # Load first State file to grab some useful information
    with open(input_path / filenames[0], "rb") as f:
        state_data = f.read()
        state = pd.state.bytes_to_state(state_data)
        level = state.world_info.location
        time_of_day = state.world_info.time_of_day
        click.echo(f"Level: {level}, Time of day: {time_of_day}")

        # Find the ego agent - it's the only one with a sensor rig
        ego_agent = next(a for a in state.agents if isinstance(a, pd.state.VehicleAgent) and a.sensors)
        ego_start_translation = ego_agent.pose[:3, 3]  # grab translation part from transform matrix
        click.echo(f"Ego agent id: {ego_agent.id}")

    # Create sensor rig object
    default_sensor_rig = pd.state.sensors_from_json(json.loads(_DEFAULT_SENSOR_RIG))

    # Create a static camera at the starting position of the ego agent
    static_camera_agent_1 = pd.state.SensorAgent(
        pose=pd.state.Pose6D.from_rpy_angles(
            x_metres=ego_start_translation[0],
            y_metres=ego_start_translation[1],
            z_metres=ego_start_translation[2] + 8.0,
            roll_degrees=0.0,
            pitch_degrees=-20.0,
            yaw_degrees=103.0,
        ),
        velocity=(0, 0, 0),
        id=pd.state.rand_agent_id(),
        sensors=default_sensor_rig,
    )

    plot_initialized = False

    click.echo("Connecting to server...", nl=False)
    session = pd.session.StepSession(request_addr=request_addr, client_cert_file=client_cert_file)
    with session:
        click.echo("done.")
        version = session.system_info.version
        click.echo(f"Server version: {version.major}.{version.minor}.{version.patch}-{version.build}")
        click.echo(f"Loading map {level}...", nl=False)
        session.load_location(level, time_of_day)
        click.echo("done")

        # Loop over all the state files
        for curr_state_index in range(0, len(filenames), _RENDER_INTERVAL):
            # Load the State file into memory so we can modify it
            with open(input_path / filenames[curr_state_index], "rb") as f:
                state_data = f.read()
            state = pd.state.bytes_to_state(state_data)

            # Replace sensor rig on ego agent
            ego_agent = next(a for a in state.agents if isinstance(a, pd.state.VehicleAgent) and a.sensors)
            ego_agent.sensors = default_sensor_rig

            # Add static camera sensor
            state.agents.append(static_camera_agent_1)

            # Send state to Step server
            session.update_state(state)

            # Check if we need to capture output frame
            if curr_state_index % (_RENDER_INTERVAL * _CAPTURE_INTERVAL) == 0:
                # Build a list of (agent, camera) that we should query
                cameras = []
                for agent in state.agents:
                    if isinstance(agent, (pd.state.VehicleAgent, pd.state.SensorAgent)) and agent.sensors:
                        for sensor in agent.sensors:
                            if isinstance(sensor, pd.state.CameraSensor) and sensor.capture_rgb:
                                cameras.append((agent.id, sensor.name))

                # Query all camera sensors
                for i, (agent_id, camera_name) in enumerate(cameras):
                    sensor_rgb_data = session.query_sensor_data(agent_id, camera_name, pd.state.SensorBuffer.RGB)
                    rgb_image = sensor_rgb_data.data_as_rgb

                    save_image(
                        rgb_output_path,
                        agent_id,
                        camera_name,
                        curr_state_index * 10,
                        cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR),
                    )

                    if preview:
                        if not plot_initialized:
                            fig, axarr = plt.subplots(2, math.ceil(len(cameras) / 2.0))
                            for ax in axarr.ravel():
                                ax.axis("off")
                            fig.set_size_inches(18, 10)
                        plot_initialized = True
                        ax = axarr.ravel()[i]
                        ax.imshow(rgb_image)
                        ax.set_xticklabels([])
                        ax.set_yticklabels([])

                if preview:
                    plt.draw()
                    plt.tight_layout()
                    plt.pause(0.01)


if __name__ == "__main__":
    cli()
