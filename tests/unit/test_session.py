import pytest

from pd.session.session import StepSession
from pd.core.errors import PdError


class TestStepSession:
    def test_step_session_init_tcp(self):
        StepSession(
            request_addr='tcp://hostname:1234'
        )

    def test_step_session_init_ssl(self):
        StepSession(
            request_addr='ssl://hostname:1234', client_cert_file='/path/to/file'
        )

    def test_step_session_init_fails_on_unknown_protocol(self):
        with pytest.raises(PdError, match=r'.*Invalid request address.*'):
            StepSession(
                request_addr='udp://hostname:1234'
            )

    def test_step_session_init_fails_on_missing_port(self):
        with pytest.raises(PdError, match=r'.*Invalid request address.*'):
            StepSession(
                request_addr='tcp://hostname'
            )

    def test_step_session_init_fails_on_missing_ssl_cert(self):
        with pytest.raises(PdError, match=r'.*certificate path missing.*'):
            StepSession(
                request_addr='ssl://hostname:1234'
            )
