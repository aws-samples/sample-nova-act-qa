import time
import pytest

from nova_act_qa.config import AppConfig
from nova_act_qa.utils import start_nova_act

"""
Fixtures for Nova ACT QA testing.

Fixtures:
    load_environment_variables: Session-scoped fixture that loads environment variables via AppConfig
    nova: Function-scoped fixture that starts and stops Nova ACT browser instance
"""


@pytest.fixture(scope="session", autouse=True)
def load_environment_variables():
    """Load environment variables via AppConfig at start of test session."""
    AppConfig()


@pytest.fixture()
def nova(request: pytest.FixtureRequest):
    """
    Start and stop Nova Act browser instance for each test, uses arguments passed to the Fixture Request.

    Args:
        request: Pytest fixture request object containing test metadata

    Yields:
        Nova Act browser instance configured for the test

    Notes:
        - Extracts test module and function names from request
        - Uses parameterized starting page
        - Automatically stops browser after test completes
    """
    test_module_name = request.module.__name__
    test_func_name = request.function.__name__
    starting_page = request.param
    nova = start_nova_act(starting_page, test_module_name, test_func_name)
    yield nova
    nova.stop()
