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

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from .decorators import validate_app_config

dotenv_encoding = "utf-8"
dotenv_path = find_dotenv(".env")


class BaseConfig(BaseSettings):
    """
    Base configuration class that inherits from Pydantic BaseSettings to validate env vars.
    This class is responsible for loading environment variables from a .env file and validating them.
    """

    model_config = SettingsConfigDict(
        env_file=dotenv_path,
        env_file_encoding=dotenv_encoding
    )

    @validate_app_config
    def __init__(self, **data):
        load_dotenv(dotenv_path, override=True, encoding=dotenv_encoding)
        super().__init__(**data)


class AppConfig(BaseConfig):
    """
    Defines the env vars required to run the app
    """

    NOVA_ACT_API_KEY: str
