"""Global pytest configuration to handle Nova Act compatibility issues."""

import os
import warnings
import pytest


def pytest_configure(config):
    """Configure pytest to work better with Nova Act SDK."""
    # Disable Nova Act keyboard monitoring during test execution
    # This prevents the stdin redirection warnings
    os.environ["NOVA_ACT_DISABLE_KEYBOARD_MONITORING"] = "1"


@pytest.fixture(autouse=True)
def suppress_nova_act_warnings():
    """Automatically suppress Nova Act keyboard monitoring warnings."""
    # Suppress thread exception warnings from Nova Act keyboard watcher
    warnings.filterwarnings(
        "ignore",
        category=pytest.PytestUnhandledThreadExceptionWarning
    )
