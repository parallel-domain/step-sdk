# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import sys
from pathlib import Path

import click
import cv2

import pd.management
import pd.session
import pd.state
import pd.umd
from pd.util import StepScriptContext, common_step_options

DEFAULT_LOCATION = ("SJ_EssexAndBradford", "v2.0.2")
DEFAULT_LIGHTING = "LS_sky_noon_mostlySunny_1250_HDS025"
DEFAULT_HEIGHT = 60.0


def get_driveway_positions_from_umd(umd_map):
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
    positions = []
    for driveway in driveways:
        lane_id = driveway.lane_segments[0]
        lane_segments = umd_map.lane_segments.get(lane_id)
        ref_line = umd_map.edges.get(lane_segments.reference_line)
        starting_point = ref_line.points[0]
        positions.append((starting_point.x, starting_point.y, starting_point.z))
    return positions


@click.command()
@common_step_options()
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
    default="./output",
    help="Output directory for images",
    show_default=True,
)
def cli(output_dir, step_options: StepScriptContext = None):
    """
    Capture driveway overhead images.
    """

    request_addr = step_options.ig
    client_cert_file = step_options.client_cert_file

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    level_name, level_version = DEFAULT_LOCATION
    umd_map = step_options.load_umd_map(level_name, level_version)

    click.echo("Connecting to server...", nl=False)
    session = pd.session.StepSession(request_addr=request_addr, client_cert_file=client_cert_file)
    with session:
        click.echo("done.")
        version = session.system_info.version
        click.echo(f"Server version: {version.major}.{version.minor}.{version.patch}-{version.build}")
        click.echo(f"Loading map {level_name}...", nl=False)
        session.load_location(level_name, DEFAULT_LIGHTING)
        click.echo("done")

        driveway_positions = get_driveway_positions_from_umd(umd_map)

        frame_count = 0
        for x, y, z in driveway_positions:
            click.echo(f"Frame {frame_count}")

            sensor = pd.state.CameraSensor(
                name="Front",
                pose=pd.state.Pose6D.from_rpy_angles(
                    x_metres=0.0, y_metres=0.0, z_metres=0.0, roll_degrees=0.0, pitch_degrees=-90.0, yaw_degrees=0.0
                ),
                width=1920,
                height=1080,
                field_of_view_degrees=90,
                capture_rgb=True,
                capture_segmentation=True,
                capture_depth=True,
                capture_instances=True,
                post_process_params=pd.state.PostProcessParams(
                    motion_blur_amount=0.0,
                ),
            )
            sensor_agent = pd.state.SensorAgent(
                id=pd.state.rand_agent_id(),
                pose=pd.state.Pose6D.from_rpy_angles(
                    x_metres=x,
                    y_metres=y,
                    z_metres=z + DEFAULT_HEIGHT,
                    roll_degrees=0.0,
                    pitch_degrees=0.0,
                    yaw_degrees=0.0,
                ),
                velocity=(0.0, 0.0, 0.0),
                sensors=[sensor],
            )
            world_info = pd.state.WorldInfo()

            state = pd.state.State(simulation_time_sec=frame_count, world_info=world_info, agents=[sensor_agent])

            # Send the environment state to server
            session.update_state(state)

            # Query camera sensor data
            sensor_data = session.query_sensor_data(sensor_agent.id, sensor.name, pd.state.SensorBuffer.RGB)
            if not (sensor_data.height > 0 and sensor_data.width > 0):
                sys.exit("Error: Failed to query sensor image from IG")
            rgb_data = sensor_data.data

            # Output the images
            # Rgb image
            image_path = output_path / f"{frame_count:04d}_rgb.png"
            if image_path.exists():
                sys.exit(f"Error: File already exists: {image_path.absolute()}")
            click.echo(f"Saving image: {image_path}")
            cv2.imwrite(str(image_path), cv2.cvtColor(rgb_data, cv2.COLOR_RGB2BGR))

            frame_count += 1


if __name__ == "__main__":
    cli()
