import math

import pd.state
from pd.internal.proto.keystone.generated.wrapper.pd_scenario_pb2 import ScenarioGenConfig, ScenarioLocation
from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorRigConfig, SensorConfig, CameraIntrinsic, \
    SensorExtrinsic
from pd.internal.proto.keystone.generated.wrapper.pd_spawn_pb2 import SpawnConfig, GeneratorConfig, SpawnConfigPreset, \
    GeneratorConfigPreset
from pd.internal.proto.keystone.generated.wrapper.pd_distributions_pb2 import CategoricalDistribution, Bucket, \
    Distribution, ConstantDistribution
from pd.internal.proto.keystone.generated.wrapper.pd_environments_pb2 import EnvironmentDefinition, EnvironmentPreset
from pd.internal.proto.keystone.generated.wrapper.pd_sim_state_pb2 import BuildSimState


def fisclose(a, b):
    return math.isclose(a, b, rel_tol=1e-05, abs_tol=1e-08)


def assert_step_server_is_alive(step_session):
    assert step_session.query_runtime_state()


def assert_query_rgb(step_session, agent_id, sensor_name):
    sensor_data = step_session.query_sensor_data(agent_id, sensor_name, pd.state.SensorBuffer.RGB)
    assert sensor_data and isinstance(sensor_data, pd.state.sensor.SensorData)
    assert sensor_data.width > 0 and sensor_data.height > 0


def preview_rgb(step_session, agent_id, sensor_name):
    import cv2
    sensor_data = step_session.query_sensor_data(agent_id, sensor_name, pd.state.SensorBuffer.RGB)
    rgb_data = sensor_data.data_as_rgb
    try:
        cv2.imshow('img', cv2.cvtColor(rgb_data, cv2.COLOR_RGB2BGR))
        cv2.waitKey(0)
    except cv2.error:
        print(f"Couldn't display GUI window, skipping preview")


def create_minimal_build_sim_state(location: str) -> BuildSimState:
    """
    Creates a minimal BuildSimState message that can be loaded in Sim
    """
    build_sim_state = BuildSimState()
    build_sim_state.locations = [
        ScenarioLocation(
            location=location,
            generator_config=GeneratorConfig(
                preset_distribution=CategoricalDistribution(buckets=[Bucket(probability=1.0)]),
                presets=[GeneratorConfigPreset()]
            )
        )
    ]
    build_sim_state.sensor_rig = SensorRigConfig()
    build_sim_state.scenario_gen = ScenarioGenConfig(
        spawn_config=SpawnConfig(
            preset_distribution=CategoricalDistribution(buckets=[Bucket(probability=1.0)]),
            presets=[SpawnConfigPreset()],
        ),
        environment=EnvironmentDefinition(
            preset_distribution=CategoricalDistribution(buckets=[Bucket(probability=1.0)]),
            presets=[EnvironmentPreset(
                time_of_day=CategoricalDistribution(buckets=[Bucket(string_value="DAY", probability=1.0)]),
                cloud_coverage=Distribution(constant=ConstantDistribution(float_value=0.0)),
                rain_intensity=Distribution(constant=ConstantDistribution(float_value=0.0)),
                fog_intensity=Distribution(constant=ConstantDistribution(float_value=0.0)),
                wetness=Distribution(constant=ConstantDistribution(float_value=0.0)),
            )]
        )
    )
    build_sim_state.sensor_rig = SensorRigConfig(
        sensor_configs=[SensorConfig(
            display_name="Front",
            camera_intrinsic=CameraIntrinsic(
                width=1920,
                height=1080,
                fov=90.0
            ),
            sensor_extrinsic=SensorExtrinsic(
                yaw=0, pitch=0, roll=0, x=0, y=0, z=0
            )
        )]
    )
    return build_sim_state
