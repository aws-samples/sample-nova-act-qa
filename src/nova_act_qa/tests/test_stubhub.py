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

test_data = [
    {
        "team_city": "Boston",
        "team_name": "Red Sox",
        "team_stadium": "Fenway Park",
    },
    {
        "team_city": "Foxborough",
        "team_location": "New England",
        "team_name": "Patriots",
        "team_stadium": "Gillete Stadium",
    },
]


@pytest.mark.parametrize("nova", ["https://stubhub.com"], indirect=True)
@pytest.mark.parametrize("test_data", test_data)
def test_game_search(nova: NovaAct, test_data):
    team_city = test_data["team_city"]
    team_location = test_data.get("team_location", team_city)
    team_name = test_data["team_name"]
    team_stadium = test_data["team_stadium"]

    nova.act(f"Search for {team_location} {team_name} tickets")
    nova.test_bool(f"A list of games for {team_location} {team_name} is rendered")
    nova.act("Select the first game")
    nova.test_bool("A dialog asking how many tickets is open, defaulting to 2")
    nova.act("Click continue")

    is_home_game = nova.check(f"Is it a home game for the {team_name}?")
    if is_home_game:
        nova.test_bool(f"The game city is {team_city}")
        nova.test_bool(f"The game stadium is {team_stadium}")
        nova.test_bool(
            f"The {team_location} {team_name} is shown in the field on the stadium seat map"
        )
