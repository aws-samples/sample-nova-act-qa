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

from enum import Enum
from typing import Any, Dict, List, TypeAlias, Union


JSONType: TypeAlias = Union[Dict[str, Any], List[Any], str, int, float, bool]

STRING_SCHEMA = {"type": "string"}


class AssertType(Enum):
    EXACT = "exact"
    CONTAINS = "contains"
