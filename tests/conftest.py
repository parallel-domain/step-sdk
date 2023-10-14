from pathlib import Path

import _pytest.skipping
import helpers as helpers_package
import pytest

################################
# Allow disabling of test skipping
# with parameter `--no-skips`


def pytest_addoption(parser):
    parser.addoption("--no-skips", action="store_true", default=False, help="disable skip marks")


@pytest.hookimpl(tryfirst=True)
def pytest_cmdline_preparse(config, args):
    if "--no-skips" not in args:
        return

    def no_skip(*args, **kwargs):
        return

    _pytest.skipping.evaluate_skip_marks = no_skip


################################


@pytest.fixture
def resources():
    return Path(__file__).parent / "resources"


@pytest.fixture
def helpers():
    """Return helper package as a fixture"""
    return helpers_package
