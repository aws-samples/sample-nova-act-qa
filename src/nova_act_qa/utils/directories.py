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

import os


script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))
user_data_dir = os.path.join(root_dir, ".nova_act", "user_data_dir")
logs_dir = os.path.join(root_dir, ".nova_act", "logs")


def initialize_nova_act_directories(module_name: str, func_name: str):
    test_logs_dir = os.path.join(logs_dir, module_name, func_name)
    test_user_data_dir = os.path.join(user_data_dir, module_name, func_name)
    os.makedirs(test_logs_dir, exist_ok=True)
    os.makedirs(test_user_data_dir, exist_ok=True)

    return test_logs_dir, test_user_data_dir
