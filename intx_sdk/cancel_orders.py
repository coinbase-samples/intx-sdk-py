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
from typing import Optional, List
from intx_sdk.base_response import BaseResponse
from intx_sdk.client import Client
from intx_sdk.credentials import Credentials
from intx_sdk.utils import append_query_param


@dataclass
class CancelOrdersRequest:
    portfolio: str
    instrument: Optional[str] = None
    side: Optional[str] = None
    instrument_type: Optional[str] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class CancelOrdersResponse(BaseResponse):
    request: CancelOrdersRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def cancel_orders(self, request: CancelOrdersRequest) -> CancelOrdersResponse:
        path = f"/orders"

        query_params = append_query_param("", 'portfolio', request.portfolio)
        query_params = append_query_param(query_params, 'instrument', request.instrument)
        query_params = append_query_param(query_params, 'side', request.side)
        query_params = append_query_param(query_params, 'instrument_type', request.instrument_type)

        response = self.client.request("DELETE", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return CancelOrdersResponse(response.json(), request)
