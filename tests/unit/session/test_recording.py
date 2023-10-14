import pytest

from pd.session.recording import ZmqRecordingReader, ZmqRecordingWriter, ZmqSocketType


def test_write_connect_record(tmp_path):
    """A connect record is written and read successfully"""
    file_path = str(tmp_path / "test.pd.bin")
    with ZmqRecordingWriter(file_path) as writer:
        writer.write_connect(timestamp=1234.5678, id_="test", type_=ZmqSocketType.REQ, address="1.1.1.1")
    reader = ZmqRecordingReader(file_path)
    record = next(reader)
    assert record.timestamp == 1234.5678
    assert record.socket_id == "test"
    assert record.socket_type == ZmqSocketType.REQ
    assert record.address == "1.1.1.1"
    with pytest.raises(StopIteration):
        next(reader)


def test_write_bind_record(tmp_path):
    """A bind record is written and read successfully"""
    file_path = str(tmp_path / "test.pd.bin")
    with ZmqRecordingWriter(file_path) as writer:
        writer.write_bind(timestamp=1234.5678, id_="test2", type_=ZmqSocketType.PUB, address="2.2.2.2")
    reader = ZmqRecordingReader(file_path)
    record = next(reader)
    assert record.timestamp == 1234.5678
    assert record.socket_id == "test2"
    assert record.socket_type == ZmqSocketType.PUB
    assert record.address == "2.2.2.2"
    with pytest.raises(StopIteration):
        next(reader)


def test_write_message_record(tmp_path):
    """A message record is written and read successfully"""
    file_path = str(tmp_path / "test.pd.bin")
    with ZmqRecordingWriter(file_path) as writer:
        writer.write_message(timestamp=1234.5678, id_="test3", type_=ZmqSocketType.PUB, data=b"\x01\x02\x03")
    reader = ZmqRecordingReader(file_path)
    record = next(reader)
    assert record.timestamp == 1234.5678
    assert record.socket_id == "test3"
    assert record.socket_type == ZmqSocketType.PUB
    assert record.message == b"\x01\x02\x03"
    with pytest.raises(StopIteration):
        next(reader)
