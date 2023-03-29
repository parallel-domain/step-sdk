# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Low-level implementation of communication over ZeroMQ
"""

import socket
import ssl
import select
import queue
from queue import Queue
import abc
from typing import List, Optional
import time
import logging
import threading

import zmq

import pd.core


logger = logging.getLogger(__name__)


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

    _TIMEOUT_RECV_MS = 300000
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
        context = zmq.Context()
        self._request_socket = context.socket(zmq.REQ)
        self._request_socket.setsockopt(zmq.RCVTIMEO, self.timeout_recv_ms)
        self._request_socket.setsockopt(zmq.LINGER, self._TIMEOUT_LINGER_MS)
        self._request_socket.connect(self.request_socket_addr)
        for l in self.listeners:
            l.on_connect_request(timestamp=time.time(), request_addr=self.request_socket_addr)
        if self.state_socket_addr:
            self._state_socket = context.socket(zmq.PUB)
            self._state_socket.bind(self.state_socket_addr)
            for l in self.listeners:
                l.on_connect_state(timestamp=time.time(), state_addr=self.state_socket_addr)
        else:
            self._state_socket = self._request_socket

    def _disconnect(self):
        if self.state_socket_addr and self._state_socket:
            self._state_socket.disconnect(self.state_socket_addr)
            for l in self.listeners:
                l.on_disconnect_state(timestamp=time.time())
        if self._request_socket:
            self._request_socket.disconnect(self.request_socket_addr)
            for l in self.listeners:
                l.on_disconnect_request(timestamp=time.time())

    def send_request_msg(self, msg_bytes: bytearray) -> bytes:
        self._request_socket.send(msg_bytes)
        resp = self._request_socket.recv()
        for l in self.listeners:
            l.on_send_request_msg(timestamp=time.time(), data=bytes(msg_bytes))
        return resp

    def send_state_msg(self, msg_bytes: bytearray):
        self._state_socket.send(msg_bytes)
        for l in self.listeners:
            l.on_send_state_msg(timestamp=time.time(), data=bytes(msg_bytes))

    def receive_state_msg(self) -> bytes:
        resp = self._state_socket.recv()
        for l in self.listeners:
            l.on_receive_state_msg(timestamp=time.time(), data=resp)
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
            target=self.proxy_worker,
            args=(
                out_queue,
                self.server_hostname, self.server_port, self.client_cert_file
            )
        )
        proxy_thread.daemon = True
        proxy_thread.start()

        try:
            client_port = out_queue.get(timeout=3)
        except queue.Empty:
            raise pd.core.errors.PdError("Connection error: failed to receive client port from TLS proxy")
        logger.debug(f"Tls Zmq transport connecting to proxy on client port {client_port}")
        self._zmq_transport = ZmqTransport(request_addr=f'tcp://127.0.0.1:{client_port}')
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
        client_socket.bind(('', 0))
        client_port = client_socket.getsockname()[1]
        out_queue.put(client_port)

        # Listen on client socket and wait for Zmq transport to connect
        logger.debug(f"TLS proxy client socket listening on port {client_port}")
        client_socket.listen()
        client_socket_handle, _ = client_socket.accept()
        client_socket.setblocking(False)
        logger.debug(f"TLS proxy client connected")

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
                                logger.error("Error: TLS connection failed")
                                server_tls_socket.close()
                                server_socket.close()
                                client_socket.close()
                                return
                        except ssl.SSLWantReadError:
                            pass
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
                        try:
                            msg_from_client = client_to_server_queue.get_nowait()
                        except queue.Empty:
                            outputs.remove(server_tls_socket)
                        else:
                            server_tls_socket.send(msg_from_client)
                            logger.debug(f"Sent msg to server (size={len(msg_from_client)})")

                for exceptional_s in exceptional:
                    if exceptional_s is client_socket_handle:
                        logger.error("Error: TLS proxy client socket exception")
                    elif exceptional_s is server_tls_socket:
                        logger.error("Error: TLS proxy server socket exception")
                    server_tls_socket.close()
                    server_socket.close()
                    client_socket.close()
                    return

        except (Exception,):
            logger.debug("Closing TLS proxy sockets")
            server_tls_socket.close()
            server_socket.close()
            client_socket.close()