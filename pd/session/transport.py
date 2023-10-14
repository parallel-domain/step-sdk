# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Low-level implementation of communication over ZeroMQ
"""

import abc
import logging
import queue
import select
import socket
import ssl
import threading
import time
from queue import Queue
from typing import List, Optional

import zmq
from zmq.error import ZMQError

from pd.core import PdError

logger = logging.getLogger(__name__)


_ZMQ_CONTEXT: Optional[zmq.Context] = None


def get_zmq_context() -> zmq.Context:
    """
    Returns the Zmq context used by transports

    Returns:
        Zmq context
    """
    global _ZMQ_CONTEXT
    if _ZMQ_CONTEXT is None:
        _ZMQ_CONTEXT = zmq.Context()
    return _ZMQ_CONTEXT


class IZmqTransportListener(abc.ABC):
    """
    Interface for observing Zmq transport messages
    """

    @abc.abstractmethod
    def on_connect_request(self, timestamp: float, request_addr: str):
        """
        Called when the transport connects to the request socket

        Args:
            timestamp: Time of connection
            request_addr: Address of request socket
        """
        pass

    @abc.abstractmethod
    def on_disconnect_request(self, timestamp: float):
        """
        Called when the transport disconnects from the request socket

        Args:
            timestamp: Time of disconnection
        """
        pass

    @abc.abstractmethod
    def on_connect_state(self, timestamp: float, state_addr: str):
        """
        Called when the transport connects to the state socket

        Args:
            timestamp: Time of connection
            state_addr: Address of state socket
        """
        pass

    @abc.abstractmethod
    def on_disconnect_state(self, timestamp: float):
        """
        Called when the transport disconnects from the state socket

        Args:
            timestamp: Time of disconnection
        """
        pass

    @abc.abstractmethod
    def on_send_request_msg(self, timestamp: float, data: bytes):
        """
        Called when the transport sends an outgoing message on the request socket

        Args:
            timestamp: Time message was sent
            data: Message data
        """
        pass

    @abc.abstractmethod
    def on_send_state_msg(self, timestamp: float, data: bytes):
        """
        Called when the transport sends an outgoing message on the state socket

        Args:
            timestamp: Time message was sent
            data: Message data
        """
        pass

    @abc.abstractmethod
    def on_receive_state_msg(self, timestamp: float, data: bytes):
        """
        Called when the transport receives an incoming message on the state socket

        Args:
            timestamp: Time the message was removed from receive buffer (and not when it was received)
            data: Message data
        """
        pass


class IZmqTransport(abc.ABC):
    """
    Interface for a transport that works over the ZeroMQ protocol.
    """

    @abc.abstractmethod
    def add_listener(self, listener: IZmqTransportListener):
        """
        Add a transport listener

        Args:
            listener: The transport listener
        """
        pass

    @abc.abstractmethod
    def send_request_msg(self, msg_bytes: bytearray) -> bytes:
        """
        Send a message over the request socket

        Args:
            msg_bytes: Message data

        Returns:
            The response data received from the server
        """
        pass

    @abc.abstractmethod
    def send_state_msg(self, msg_bytes: bytearray):
        """
        Send a message over the state socket

        Args:
            msg_bytes: Message data
        """
        pass

    @abc.abstractmethod
    def receive_state_msg(self) -> bytes:
        """
        Receive next message from the state socket

        Returns:
            The message data
        """
        pass


class ZmqTransport(IZmqTransport):
    """
    Provides the ZeroMQ transport for communication with a server

    This class provides functionality to send bytes over ZeroMQ to one of two
    sockets: request or state.
    """

    _TIMEOUT_RECV_MS = 600_000
    _TIMEOUT_LINGER_MS = 0

    def __init__(self, request_addr: str, state_addr: Optional[str] = None):
        self.request_socket_addr = request_addr
        self.state_socket_addr = state_addr
        self._request_socket = None
        self._state_socket = None
        self.listeners: List[IZmqTransportListener] = []
        self.timeout_recv_ms = self._TIMEOUT_RECV_MS

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, *args):
        self._disconnect()

    def add_listener(self, listener: IZmqTransportListener):
        self.listeners.append(listener)

    def _connect(self):
        context = get_zmq_context()
        self._request_socket = context.socket(zmq.REQ)
        self._request_socket.setsockopt(zmq.RCVTIMEO, self.timeout_recv_ms)
        self._request_socket.setsockopt(zmq.LINGER, self._TIMEOUT_LINGER_MS)
        self._request_socket.connect(self.request_socket_addr)
        for ll in self.listeners:
            ll.on_connect_request(timestamp=time.time(), request_addr=self.request_socket_addr)
        if self.state_socket_addr:
            self._state_socket = context.socket(zmq.PUB)
            self._state_socket.bind(self.state_socket_addr)
            for ll in self.listeners:
                ll.on_connect_state(timestamp=time.time(), state_addr=self.state_socket_addr)
        else:
            self._state_socket = self._request_socket

    def _disconnect(self):
        if self.state_socket_addr and self._state_socket:
            self._state_socket.disconnect(self.state_socket_addr)
            for ll in self.listeners:
                ll.on_disconnect_state(timestamp=time.time())
            self._state_socket.close()
        if self._request_socket:
            self._request_socket.disconnect(self.request_socket_addr)
            for ll in self.listeners:
                ll.on_disconnect_request(timestamp=time.time())
            self._request_socket.close()

    def send_request_msg(self, msg_bytes: bytearray) -> bytes:
        self._request_socket.send(msg_bytes)
        try:
            resp = self._request_socket.recv()
        except ZMQError as e:
            raise PdError(
                "Timed out while waiting for the server to respond. "
                "Please check that the server is running and the server address is correct. "
                "Please contact support@paralleldomain.com for support. "
                f"Error: {e.strerror} ({e.errno})"
            )
        for ll in self.listeners:
            ll.on_send_request_msg(timestamp=time.time(), data=bytes(msg_bytes))
        return resp

    def send_state_msg(self, msg_bytes: bytearray):
        self._state_socket.send(msg_bytes)
        for ll in self.listeners:
            ll.on_send_state_msg(timestamp=time.time(), data=bytes(msg_bytes))

    def receive_state_msg(self) -> bytes:
        resp = self._state_socket.recv()
        for ll in self.listeners:
            ll.on_receive_state_msg(timestamp=time.time(), data=resp)
        return resp


class TlsProxyForZmqTransport(IZmqTransport):
    __SOCKET_BUFFER_SIZE = 4096

    def __init__(self, server_hostname: str, server_port: int, client_cert_file: str):
        """
        Zmq transport that works over a TLS connection

        This Zmq transport requires that the server address is a TLS endpoint.
        The transport supports only the request socket - state socket is not supported.

        Args:
            server_hostname: Address of TLS endpoint
            server_port: Port number of TLS endpoint
            client_cert_file: Path to the credentials certificate
        """
        # This class implements a proxy worker which is run in a separate thread
        # The proxy worker does the following:
        #   1. Creates an intermediate socket and directs the Zmq transport to connect to that socket
        #   2. Connects to the server at the TLS endpoint with an SSL socket
        #   3. Runs a main loop where it relays messages between the intermediate socket and the TLS endpoint.
        #      The SSL socket automatically handles all of the encryption and decryption of the messages
        self.server_hostname = server_hostname
        self.server_port = server_port
        self.client_cert_file = client_cert_file
        self.timeout_recv_ms = None
        self._zmq_transport = None  # instantiate on connect

    def __enter__(self):
        self._connect()
        self._zmq_transport.__enter__()
        return self

    def __exit__(self, *args):
        self._zmq_transport.__exit__(*args)

    def _connect(self):
        out_queue = Queue()
        proxy_thread = threading.Thread(
            target=self.proxy_worker, args=(out_queue, self.server_hostname, self.server_port, self.client_cert_file)
        )
        proxy_thread.daemon = True
        proxy_thread.start()

        try:
            client_port = out_queue.get(timeout=3)
        except queue.Empty:
            raise PdError("Connection error: failed to receive client port from TLS proxy")
        logger.debug(f"Tls Zmq transport connecting to proxy on client port {client_port}")
        self._zmq_transport = ZmqTransport(request_addr=f"tcp://127.0.0.1:{client_port}")
        if self.timeout_recv_ms:
            self._zmq_transport.timeout_recv_ms = self.timeout_recv_ms

    def add_listener(self, listener: IZmqTransportListener):
        self._zmq_transport.add_listener(listener)

    def send_request_msg(self, msg_bytes: bytearray) -> bytes:
        return self._zmq_transport.send_request_msg(msg_bytes)

    def send_state_msg(self, msg_bytes: bytearray):
        self._zmq_transport.send_state_msg(msg_bytes)

    def receive_state_msg(self) -> bytes:
        return self._zmq_transport.receive_state_msg()

    @staticmethod
    def proxy_worker(out_queue: Queue, server_hostname: str, server_port: int, certificate_path: str):
        skip_tls = False  # for debugging purposes

        # Create client socket and send back the client port number
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.bind(("", 0))
        client_port = client_socket.getsockname()[1]
        out_queue.put(client_port)

        # Listen on client socket and wait for Zmq transport to connect
        logger.debug(f"TLS proxy client socket listening on port {client_port}")
        client_socket.listen()
        client_socket_handle, _ = client_socket.accept()
        client_socket.setblocking(False)
        logger.debug("TLS proxy client connected")

        # Connect to TLS server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if skip_tls:
            server_tls_socket = server_socket
            server_tls_socket.connect((server_hostname, server_port))
        else:
            ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

            ssl_context.load_cert_chain(certificate_path)
            server_tls_socket = ssl_context.wrap_socket(
                server_socket,
                server_hostname=server_hostname,
                server_side=False,
            )
            server_tls_socket.connect((server_hostname, server_port))
            logger.debug(f"Connected to TLS server {server_hostname}:{server_port}")
            logger.debug(f"TLS version is {server_tls_socket.version()}")
            logger.debug(f"TLS cipher is {server_tls_socket.cipher()}")
        server_tls_socket.setblocking(False)

        # Main loop for proxy
        inputs = [client_socket_handle, server_tls_socket]
        outputs = []
        client_to_server_queue = Queue()
        client_to_server_retry_queue = Queue(maxsize=1)
        server_to_client_queue = Queue()
        try:
            while True:
                readable, writable, exceptional = select.select(inputs, outputs, inputs)

                for readable_s in readable:
                    if readable_s is client_socket_handle:
                        msg_from_client = readable_s.recv(TlsProxyForZmqTransport.__SOCKET_BUFFER_SIZE)
                        logger.debug(f"Received msg from client (size={len(msg_from_client)})")
                        client_to_server_queue.put(msg_from_client)
                        if server_tls_socket not in outputs:
                            outputs.append(server_tls_socket)

                    elif readable_s is server_tls_socket:
                        try:
                            msg_from_server = readable_s.recv(TlsProxyForZmqTransport.__SOCKET_BUFFER_SIZE)
                            if not msg_from_server:
                                logger.error(
                                    "Error: Failed to establish a secure connection to the server. "
                                    "Please check that you have the correct server address and that you're "
                                    "using the correct credentials file. "
                                    "Please contact support@paralleldomain.com for support."
                                )
                                server_tls_socket.close()
                                server_socket.close()
                                client_socket.close()
                                # The main thread will wait on a recv() at this point until it times out
                                # Since Python3.5, there is no way to interrupt it
                                return
                        except (ssl.SSLWantReadError, ssl.SSLWantWriteError) as e:
                            # Retry
                            logger.debug(f"Suppressed SSL error {e.__class__.__name__} {str(e)}")
                        except ssl.SSLError as e:
                            # Retry if handshake suspended
                            if e.errno != ssl.SSL_ERROR_WANT_X509_LOOKUP:
                                raise
                            logger.debug(f"Suppress SSL error {e.__class__.__name__} {str(e)}")
                        else:
                            if not skip_tls:
                                data_left = server_tls_socket.pending()
                                while data_left:
                                    msg_from_server += server_tls_socket.recv(data_left)
                                    data_left = server_tls_socket.pending()
                            logger.debug(f"Received msg from server (size={len(msg_from_server)})")
                            server_to_client_queue.put(msg_from_server)
                            if client_socket_handle not in outputs:
                                outputs.append(client_socket_handle)

                for writable_s in writable:
                    if writable_s is client_socket_handle:
                        try:
                            msg_from_server = server_to_client_queue.get_nowait()
                        except queue.Empty:
                            outputs.remove(client_socket_handle)
                        else:
                            client_socket_handle.send(msg_from_server)
                            logger.debug(f"Sent msg to client (size={len(msg_from_server)})")

                    if writable_s is server_tls_socket:
                        # We might need to retry writes when the TLS socket throws an error
                        # At this point we have already popped the message from the queue
                        # There's no way to put it back, and no way to peek before popping either
                        # So instead we throw it in a retry queue, and prioritize reading from
                        # the retry queue first
                        try:
                            # Try to get from the retry queue first, then the actual queue
                            try:
                                msg_from_client = client_to_server_retry_queue.get_nowait()
                            except queue.Empty:
                                msg_from_client = client_to_server_queue.get_nowait()
                        except queue.Empty:
                            outputs.remove(server_tls_socket)
                        else:
                            if not msg_from_client:
                                # Client connection must have ended
                                logger.debug("Received empty message from client. Closing TLS socket")
                                server_tls_socket.close()
                                server_socket.close()
                                client_socket.close()
                                return
                            try:
                                server_tls_socket.send(msg_from_client)
                                logger.debug(f"Sent msg to server (size={len(msg_from_client)})")
                            except (ssl.SSLWantReadError, ssl.SSLWantWriteError) as e:
                                # Retry
                                logger.debug(f"Suppressed SSL error {e.__class__.__name__} {str(e)}")
                                client_to_server_retry_queue.put(msg_from_client)
                            except ssl.SSLError as e:
                                # Retry if handshake suspended
                                if e.errno != ssl.SSL_ERROR_WANT_X509_LOOKUP:
                                    raise
                                logger.debug(f"Suppress SSL error {e.__class__.__name__} {str(e)}")
                                client_to_server_retry_queue.put(msg_from_client)

                for exceptional_s in exceptional:
                    if exceptional_s is client_socket_handle:
                        logger.error("Error: TLS proxy client socket exception")
                    elif exceptional_s is server_tls_socket:
                        logger.error("Error: TLS proxy server socket exception")
                    server_tls_socket.close()
                    server_socket.close()
                    client_socket.close()
                    return

        except (Exception,) as e:
            logger.error(
                "Secure connection with the server was interrupted. "
                "Please contact support@paralleldomain.com for support. "
                f"Error: Closing TLS socket due to {e.__class__.__name__} {str(e)}"
            )
            server_tls_socket.close()
            server_socket.close()
            client_socket.close()
