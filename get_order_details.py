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
from base_response import BaseResponse
from client import Client
from credentials import Credentials
from utils import append_query_param


@dataclass
class GetOrderDetailsRequest:
    order_id: str
    portfolio: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetOrderDetailsResponse(BaseResponse):
    request: GetOrderDetailsRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def get_order_details(self, request: GetOrderDetailsRequest) -> GetOrderDetailsResponse:
        path = f"/orders/{request.order_id}"

        query_params = append_query_param("", 'portfolio', request.portfolio)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return GetOrderDetailsResponse(response.json(), request)
