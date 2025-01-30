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

from dataclasses import dataclass, asdict
from typing import Optional, List
from intx_sdk.base_response import BaseResponse
from intx_sdk.client import Client
from intx_sdk.credentials import Credentials


@dataclass
class CreateOrderRequest:
    client_order_id: str
    side: str
    size: str
    tif: str
    instrument: str
    type: str
    price: Optional[str] = None
    stop_price: Optional[str] = None
    stop_limit_price: Optional[str] = None
    expire_time: Optional[str] = None
    portfolio: Optional[str] = None
    user: Optional[str] = None
    stp_mode: Optional[str] = None
    post_only: Optional[str] = None
    close_only: Optional[str] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class CreateOrderResponse(BaseResponse):
    request: CreateOrderRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def create_order(self, request: CreateOrderRequest) -> CreateOrderResponse:
        path = "/orders"
        body = {k: v for k, v in asdict(request).items() if v is not None}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateOrderResponse(response.json(), request)
