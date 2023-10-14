# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Utilities related to recording a session
"""

import logging
from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes

from pd.internal.log.log_pb2 import Action
from pd.session.transport import IZmqTransportListener


# This must match log.proto
class ZmqSocketType(IntEnum):
    UNKNOWN = 0
    REQ = 1
    SUB = 2
    PUB = 3


@dataclass(frozen=True)
class ZmqRecord:
    """
    Represents a single message in a Recording
    """

    timestamp: float
    socket_type: ZmqSocketType
    socket_id: int
    address: Optional[str]
    message: Optional[bytes]


class ZmqRecordingWriter:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, "wb")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write_connect(self, timestamp: float, id_: str, type_: ZmqSocketType, address: str):
        action = Action()
        action.timestamp = timestamp
        action.socket_info.id = id_
        action.socket_info.type = type_
        action.connect.address = address
        self._write_action(action)

    def write_bind(self, timestamp: float, id_: str, type_: ZmqSocketType, address: str):
        action = Action()
        action.timestamp = timestamp
        action.socket_info.id = id_
        action.socket_info.type = type_
        action.bind.address = address
        self._write_action(action)

    def write_message(self, timestamp: float, id_: str, type_: ZmqSocketType, data: bytes):
        action = Action()
        action.timestamp = timestamp
        action.socket_info.id = id_
        action.socket_info.type = type_
        action.message.data = data
        self._write_action(action)

    def _write_action(self, action: Action):
        self.file.write(_VarintBytes(action.ByteSize()))
        self.file.write(action.SerializeToString())
        self.file.flush()


class ZmqRecordingReader:
    def __init__(self, path: str):
        self.file = open(path, "rb")
        self.size_read = 0

    def __iter__(self):
        return self

    def __next__(self) -> ZmqRecord:
        if not self.file:
            raise StopIteration

        # Successively read more bytes until we can decode a varint representing the size
        buffer = bytearray()
        byte = self.file.read(1)
        self.size_read += len(byte)
        size = 0
        while byte:
            buffer.extend(byte)
            try:
                size, _ = _DecodeVarint32(buffer, 0)
                break
            except IndexError:
                byte = self.file.read(1)
                self.size_read += len(byte)

        if not size:
            raise StopIteration
        data = self.file.read(size)
        self.size_read += len(data)
        if len(data) < size:
            logger = logging.getLogger(__name__)
            logger.warning(f"Failed to read record - {size} bytes needed but only {len(data)} bytes read")
            raise StopIteration
        action = Action()
        action.ParseFromString(data)
        address = None
        address = action.connect.address if action.HasField("connect") else address
        address = action.bind.address if action.HasField("bind") else address
        message = action.message.data if action.HasField("message") else None
        record = ZmqRecord(
            timestamp=action.timestamp,
            socket_type=ZmqSocketType(action.socket_info.type),
            socket_id=action.socket_info.id,
            address=address,
            message=message,
        )
        return record


class RecordingZmqTransportListener(IZmqTransportListener):
    """
    Listens to ZmqTransport events and records them to a log.
    """

    def __init__(self, path: str):
        self.writer = ZmqRecordingWriter(path=path)
        self.writer.__enter__()

    def close(self):
        self.writer.__exit__(None, None, None)

    def on_connect_request(self, timestamp: float, request_addr: str):
        self.writer.write_connect(timestamp=timestamp, id_="request", type_=ZmqSocketType.REQ, address=request_addr)

    def on_disconnect_request(self, timestamp: float):
        pass

    def on_connect_state(self, timestamp: float, state_addr: str):
        self.writer.write_bind(timestamp=timestamp, id_="state_publisher", type_=ZmqSocketType.PUB, address=state_addr)

    def on_disconnect_state(self, timestamp: float):
        pass

    def on_send_request_msg(self, timestamp: float, data: bytes):
        self.writer.write_message(timestamp=timestamp, id_="request", type_=ZmqSocketType.REQ, data=data)

    def on_send_state_msg(self, timestamp: float, data: bytes):
        self.writer.write_message(timestamp=timestamp, id_="state_publisher", type_=ZmqSocketType.PUB, data=data)

    def on_receive_state_msg(self, timestamp: float, data: bytes):
        pass
