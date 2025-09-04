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
