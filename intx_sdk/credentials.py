# Copyright 2024-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#  limitations under the License.

import os
import json
from dataclasses import dataclass


@dataclass
class Credentials:
    access_key: str
    passphrase: str
    signing_key: str

    @staticmethod
    def from_json(data: str) -> 'Credentials':
        credentials_dict = json.loads(data)
        return Credentials(
            access_key=credentials_dict['accessKey'],
            passphrase=credentials_dict['passphrase'],
            signing_key=credentials_dict['signingKey']
        )

    @staticmethod
    def from_env(variable_name: str) -> 'Credentials':
        env_var = os.getenv(variable_name)
        if not env_var:
            raise EnvironmentError(
                f"{variable_name} not set as environment variable")
        return Credentials.from_json(env_var)
