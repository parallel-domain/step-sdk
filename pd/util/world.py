# Copyright (c) 2022 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from pd.session import StepSession
from pd.state import Pose6D, SensorAgent, SensorBuffer, State, rand_agent_id
from pd.state.sensor import CameraSensor, DistortionParams


def get_altitude_estimate(x: float, y: float, state: State, session: StepSession, z_initial: float = 100.0) -> float:
    camera = CameraSensor(
        name="altitude_estimation_001",
        pose=Pose6D.from_rpy_angles(0, 0, 0, 0, -90, 0),
        width=1,
        height=1,
        field_of_view_degrees=1.0,
        capture_depth=True,
        distortion_params=DistortionParams(cx=0.5, cy=0.5),
    )

    camera_agent = SensorAgent(
        id=rand_agent_id(),
        pose=Pose6D.from_rpy_angles(x, y, z_initial + 1, 0, 0, 0),
        velocity=(0, 0, 0),
        sensors=[camera],
    )

    state.agents.append(camera_agent)
    session.update_state(state)

    sensor_data = session.query_sensor_data(camera_agent.id, camera.name, SensorBuffer.DEPTH)
    depth = sensor_data.data_as_depth[0, 0]

    return z_initial + 1 - depth
