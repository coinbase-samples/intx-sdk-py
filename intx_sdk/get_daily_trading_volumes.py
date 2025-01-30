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

from dataclasses import dataclass
from typing import List, Optional
from intx_sdk.base_response import BaseResponse
from intx_sdk.client import Client
from intx_sdk.credentials import Credentials
from intx_sdk.utils import append_pagination_params, append_query_param, PaginationParams


@dataclass
class GetDailyTradingVolumesRequest:
    instruments: str
    time_from: Optional[str] = None
    show_other: Optional[str] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetDailyTradingVolumesResponse(BaseResponse):
    request: GetDailyTradingVolumesRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def get_daily_trading_volumes(self, request: GetDailyTradingVolumesRequest) -> GetDailyTradingVolumesResponse:
        path = "/instruments/volumes/daily"

        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, 'instruments', request.instruments)
        query_params = append_query_param(query_params, 'time_from', request.time_from)
        query_params = append_query_param(query_params, 'show_other', request.show_other)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return GetDailyTradingVolumesResponse(response.json(), request)
