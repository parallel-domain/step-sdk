# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import json
import logging
import time
from typing import Optional, overload

from pd.data_lab.context import validate_instance_address
from pd.label_engine import DEFAULT_LABEL_ENGINE_CONFIG_NAME, LabelData, load_pipeline_config
from pd.session import LabelEngineSession

logger = logging.getLogger(__name__)


class LabelEngineInstance:
    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        address: Optional[str] = None,
        config_name: str = DEFAULT_LABEL_ENGINE_CONFIG_NAME,
    ):
        ...

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        address: Optional[str] = None,
        config: str,
    ):
        ...

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        address: Optional[str] = None,
        config_name: Optional[str] = DEFAULT_LABEL_ENGINE_CONFIG_NAME,
        config: Optional[str] = None,
    ):
        """
        Create a label engine instance for an existing remote label engine server

        Args:
            name: Instance name. Required for cloud mode
            address: Instance address. Used in local mode
            config_name: Name of the config to load on session creation
            config: Content of the config to load on session creation
        """
        super().__init__()
        self.address = address
        self.name = name
        self.session: Optional[LabelEngineSession] = None
        self._config_name = config_name
        self._config = config
        self._unique_scene_name = None
        self._client_cert_file = None
        self.output_path_to_generator_type = None

    def create_session(self, unique_scene_name: str):
        if self.session is None:
            self.session = LabelEngineSession(request_addr=self.address, client_cert_file=self._client_cert_file)
            self.session.transport.timeout_recv_ms = 600_000
            self.session.__enter__()
            logger.info("Started Label Engine Session!")

            if self._config_name is not None:
                self.load_config(config_name=self._config_name, unique_scene_name=unique_scene_name)
            elif self._config is not None:
                self.configure(config=self._config, unique_scene_name=unique_scene_name)

        return self.session

    def end_session(self):
        if self.session is not None:
            self.session.__exit__()
            self.session = None
            logger.info("Ended Label Engine Session!")

    def setup(self, unique_scene_name: str):
        if self._client_cert_file is None:
            self.address, self.name, self._client_cert_file = validate_instance_address(
                instance_type="le", address=self.address, name=self.name
            )
        self.create_session(unique_scene_name=unique_scene_name)

    def cleanup(self):
        self.end_session()

    def configure(self, unique_scene_name: str, config: str) -> None:
        self._config = config
        self._unique_scene_name = unique_scene_name
        self.session.configure(scene_name=self._unique_scene_name, config=config)

    def load_config(self, unique_scene_name: str, config_name: str = DEFAULT_LABEL_ENGINE_CONFIG_NAME) -> None:
        self._config_name = config_name
        le_config = load_pipeline_config(config_name)
        self.configure(config=le_config, unique_scene_name=unique_scene_name)

    def get_annotation_data(
        self, frame_timestamp: str, sensor_id: Optional[int], sensor_name: Optional[str], stream_name: str
    ) -> LabelData:
        self.wait_for_annotation_data(
            frame_timestamp=frame_timestamp, sensor_id=sensor_id, sensor_name=sensor_name, stream_name=stream_name
        )
        return self.session.request_annotation_data(
            scene_name=self._unique_scene_name,
            timestamp=frame_timestamp,
            label=stream_name,
            sensor_id_and_name=None if sensor_id is None or sensor_name is None else (sensor_id, sensor_name),
        )

    def wait_for_annotation_data(
        self,
        frame_timestamp: str,
        sensor_id: Optional[int],
        sensor_name: Optional[str],
        stream_name: str,
        seconds_between_requests: float = 0.1,
    ) -> None:
        while not self.session.query_annotation_status(
            scene_name=self._unique_scene_name,
            timestamp=frame_timestamp,
            label=stream_name,
            sensor_id_and_name=None if sensor_id is None or sensor_name is None else (sensor_id, sensor_name),
        ):
            time.sleep(seconds_between_requests)

    @property
    def config_name(self) -> str:
        return self._config_name
