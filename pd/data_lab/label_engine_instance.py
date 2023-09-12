# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import logging
import time
from typing import Optional, List, overload

from pd.core import PdError
from pd.data_lab.context import get_datalab_context
from pd.label_engine import load_pipeline_config, LabelData
from pd.management import Ig
from pd.session import LabelEngineSession

logger = logging.getLogger(__name__)


class LabelEngineInstance:
    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        address: Optional[str] = None,
        config_name: str = "pipeline_minimal",
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
        config_name: Optional[str] = "pipeline_minimal",
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
        context = get_datalab_context()
        self._client_cert_file = context.client_cert_file
        self.session: Optional[LabelEngineSession] = None
        self._config_name = config_name
        self._config = config
        self._unique_scene_name = None

        if name and address:
            raise PdError("Only one of 'name' or 'address' can be specified for RenderInstance.")
        if not context.is_mode_local and not name:
            raise PdError("A 'name' is required in RenderInstance when running in cloud mode.")

        if context.is_mode_local:
            # Local mode, use local address if none is provided
            self.address = self.address or "tcp://localhost:9004"
        else:
            # Cloud mode, resolve the address
            try:
                ig = next(ig for ig in Ig.list() if ig.name == name)
            except StopIteration:
                raise PdError(
                    f"Couldn't find a render instance with the name '{name}'. "
                    "Please verify that the name is correct."
                )
            if context.fail_on_version_mismatch:
                if ig.ig_version != context.version:
                    raise PdError(
                        f"There's a mismatch between the selected Data Lab version ({context.version}) "
                        f"and the version of the render instance ({ig.ig_version}). "
                        "To disable this check, pass fail_on_version_mismatch=False to setup_datalab()."
                    )
            self.address = ig.le_url
            if self.address is None:
                raise PdError("Render Instance doesn't have a label engine server.")

    def set_unique_scene_name(self, unique_scene_name: str):
        self._unique_scene_name = unique_scene_name

    def create_session(self):
        if self.session is None:
            self.session = LabelEngineSession(request_addr=self.address, client_cert_file=self._client_cert_file)
            self.session.transport.timeout_recv_ms = 600_000
            self.session.__enter__()
            logger.info("Started Label Engine Session!")

            if self._config_name is not None:
                self.load_config(config_name=self._config_name)
            elif self._config is not None:
                self.configure(config=self._config)

        return self.session

    def end_session(self):
        if self.session is not None:
            self.session.__exit__()
            self.session = None
            logger.info("Ended Label Engine Session!")

    def __enter__(self) -> LabelEngineSession:
        return self.create_session()

    def __exit__(self, *args):
        self.end_session()

    def configure(self, config: str) -> None:
        self._config = config
        self.session.configure(scene_name=self._unique_scene_name, config=config)

    def load_config(self, config_name: str = "pipeline_minimal") -> None:
        self._config_name = config_name
        le_config = load_pipeline_config(config_name)
        self.configure(config=le_config)

    def get_annotation_data(self, frame_timestamp: str, sensor_id: int, sensor_name: str,
                            stream_name: str) -> LabelData:
        self.wait_for_annotation_data(frame_timestamp=frame_timestamp, sensor_id=sensor_id, sensor_name=sensor_name,
                                      stream_name=stream_name)
        return self.session.request_annotation_data(scene_name=self._unique_scene_name,
                                                    timestamp=frame_timestamp, label=stream_name,
                                                    sensor_id_and_name=(sensor_id, sensor_name))

    def wait_for_annotation_data(
        self, frame_timestamp: str, sensor_id: int, sensor_name: str, stream_name: str,
        seconds_between_requests: float = 0.1
    ) -> None:

        while not self.session.query_annotation_status(scene_name=self._unique_scene_name,
                                                       timestamp=frame_timestamp, label=stream_name,
                                                       sensor_id_and_name=(sensor_id, sensor_name)):
            time.sleep(seconds_between_requests)
