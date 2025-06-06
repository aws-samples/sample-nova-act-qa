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

from nova_act_qa.utils.nova_act import NovaAct

NOVA_ACT_URL = "https://nova.amazon.com/act"


@pytest.mark.parametrize("nova", ["https://nova.amazon.com"], indirect=True)
def test_navigation(nova: NovaAct):
    nova.test_bool("Is Act on the side nav?")
    nova.act("Go to the Act page")
    assert nova.page.url == NOVA_ACT_URL


@pytest.mark.parametrize("nova", ["https://nova.amazon.com/act"], indirect=True)
def test_landing_page(nova: NovaAct):
    nova.test_bool("Am I on the Nova Act landing page?")
    nova.test_bool("Is there a Get Started section?")
    nova.test_str("The pip install command for the SDK", "pip install nova-act")
    nova.test_str("API Key button text", "Generate key")
