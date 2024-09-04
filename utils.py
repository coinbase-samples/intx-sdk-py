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

from dataclasses import asdict, dataclass
from typing import Dict, Optional, Union, List


@dataclass
class PaginationParams:
    result_limit: str = ''
    result_offset: str = ''

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)


def append_query_param(query_params: str, key: str, value: Optional[Union[str, List[str]]]) -> str:
    if value:
        if isinstance(value, list):
            for v in value:
                query_params = f"{query_params}&{key}={v}" if query_params else f"{key}={v}"
        else:
            query_params = f"{query_params}&{key}={value}" if query_params else f"{key}={value}"
    return query_params


def append_pagination_params(query_params: str, pagination: Optional[PaginationParams]) -> str:
    if pagination:
        query_params = append_query_param(query_params, 'result_limit', pagination.result_limit)
        query_params = append_query_param(query_params, 'result_offset', pagination.result_offset)
    return query_params
