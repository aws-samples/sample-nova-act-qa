# Copyright Amazon Inc

# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
