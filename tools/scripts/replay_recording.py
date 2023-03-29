import time
import logging.config
import click
import contextlib
from typing import List, Tuple

import flatbuffers

from pd.internal.fb.generated.python import pdMessage, pdEnableStateStream, pdLoadLocation
from pd.internal.fb.generated.python.pdMessageType import pdMessageType
from pd.session.session import ZmqTransport
from pd.session.recording import ZmqSocketType, ZmqRecordingReader


@click.command()
@click.argument('filepaths', nargs=-1, type=click.Path(exists=True, dir_okay=False))
@click.option(
    '-s', '--server',
    default='tcp://127.0.0.1:9000',
    help="Address of pdImageGen server (eg. tcp://127.0.0.1:9000)",
    show_default=True
)
@click.option(
    '-c', '--client',
    default='tcp://127.0.0.1:9001',
    help="Address of local machine (eg. tcp://127.0.0.1:9001)",
    show_default=True
)
@click.option(
    '--dry-run/--live-run',
    default=False,
    help="Parse recording but don't wait or send any messages"
)
@click.option(
    '--replace-level',
    type=click.Tuple([str, str]),
    multiple=True,
    help="Replace names of levels that are loaded"
)
def cli(filepaths, server: str, client: str, dry_run: bool, replace_level: List[Tuple[str, str]]):
    """
    Replay a PD Stream recording
    """
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger()

    # This map is used to replace names of levels that are loaded
    replace_level_lookup = {orig: new for orig, new in replace_level}

    transport = ZmqTransport(request_addr=server, state_addr=client) \
        if not dry_run else contextlib.suppress()
    with transport:
        for filepath in filepaths:
            local_start_time = time.time()
            record_start_time = None
            logger.info(f"Playing log: {filepath}")
            for record in ZmqRecordingReader(filepath):
                record_start_time = record_start_time or record.timestamp

                # Spin until we hit the desired local time
                if not dry_run:
                    while time.time() - local_start_time < record.timestamp - record_start_time:
                        pass

                pd_message = None
                if record.message:
                    message = record.message

                    pd_message = pdMessage.pdMessage.GetRootAspdMessage(record.message, 0)

                    # Replace client address
                    if pd_message.MessageType() == pdMessageType.pdEnableStateStream:
                        pd_message_ss = pdEnableStateStream.pdEnableStateStream()
                        pd_message_ss.Init(pd_message.Message().Bytes, pd_message.Message().Pos)
                        old_address = pd_message_ss.Address().decode()

                        # Intercept EnableStateStream and reroute to local IG address
                        builder = flatbuffers.Builder(1024)
                        address = builder.CreateString(client)

                        pdEnableStateStream.pdEnableStateStreamStart(builder)
                        pdEnableStateStream.pdEnableStateStreamAddAddress(builder, address)
                        state_msg = pdEnableStateStream.pdEnableStateStreamEnd(builder)

                        pdMessage.pdMessageStart(builder)
                        pdMessage.pdMessageAddMessageType(builder, pdMessageType.pdEnableStateStream)
                        pdMessage.pdMessageAddMessage(builder, state_msg)
                        msg = pdMessage.pdMessageEnd(builder)

                        builder.Finish(msg)
                        message = builder.Output()
                        logger.info(f"EnableStateStream changed from {old_address} to {client}")

                    # Replace maps
                    if pd_message.MessageType() == pdMessageType.pdLoadLocation:
                        pd_message_ld = pdLoadLocation.pdLoadLocation()
                        pd_message_ld.Init(pd_message.Message().Bytes, pd_message.Message().Pos)
                        old_location = pd_message_ld.LocationName().decode()
                        if old_location in replace_level_lookup:
                            new_location = replace_level_lookup[old_location]
                            builder = flatbuffers.Builder(1024)
                            location_name = builder.CreateString(new_location)
                            time_of_day = builder.CreateString(pd_message_ld.TimeOfDay().decode())

                            pdLoadLocation.pdLoadLocationStart(builder)
                            pdLoadLocation.pdLoadLocationAddLocationName(builder, location_name)
                            pdLoadLocation.pdLoadLocationAddTimeOfDay(builder, time_of_day)
                            state_msg = pdLoadLocation.pdLoadLocationEnd(builder)

                            pdMessage.pdMessageStart(builder)
                            pdMessage.pdMessageAddMessageType(builder, pdMessageType.pdLoadLocation)
                            pdMessage.pdMessageAddMessage(builder, state_msg)
                            msg = pdMessage.pdMessageEnd(builder)

                            builder.Finish(msg)
                            message = builder.Output()
                            logger.info(f"LoadLocation changed from {old_location} to {new_location}")
                        else:
                            logger.info(f"LoadLocation {old_location}")

                    if pd_message:
                        message_type_name = next(k for k, v in pdMessageType.__dict__.items() if v == pd_message.MessageType())
                    else:
                        message_type_name = 'none'
                    logger.info(
                        f"Time: {record.timestamp-record_start_time:.6f}s, "
                        f"Type: {ZmqSocketType(record.socket_type).name}, "
                        f"MessageType: {message_type_name}"
                    )

                    # Send out the recorded message on appropriate socket
                    if not dry_run:
                        if record.socket_type == ZmqSocketType.REQ:
                            transport.send_request_msg(message)
                        elif record.socket_type == ZmqSocketType.PUB:
                            transport.send_state_msg(message)


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'brief': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'brief',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}


if __name__ == '__main__':
    cli()
