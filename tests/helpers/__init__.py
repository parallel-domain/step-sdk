import math

import pd.state


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
