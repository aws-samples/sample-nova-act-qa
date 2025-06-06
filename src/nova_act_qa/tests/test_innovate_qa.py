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


@pytest.mark.parametrize("nova", ["https://innovateqaevents.com/"], indirect=True)
def test_landing_page(nova: NovaAct):
    nova.test_bool("Am I on the Innovate QA landing page?")
    nova.test_str("Conference date", "June 5, 2025")
    nova.test_str("Conference location", "Hilton Garden Inn 1800 NW Gilman Blvd Issaquah, WA")


@pytest.mark.parametrize(
    "nova", ["https://innovateqaevents.com/2025-program-speakers"], indirect=True
)
def test_program_speakers_page(nova: NovaAct):
    nova.test_str("Agenda on June 4", "Social Networking")
    nova.test(
        "3 Agenda columns on June 5",
        ["Leadership Track", "IC Track", "Workshop/Discussion"],
        {"type": "array", "items": {"type": "string"}},
    )
    contact_button_text = "Drop us a line!"
    contact_button = nova.page.get_by_role("button", name=contact_button_text)
    contact_button.scroll_into_view_if_needed()
    nova.act(f"Click the {contact_button_text} button")
    nova.act("Click the Send button")
    nova.test_bool("There is an input validation error message")
