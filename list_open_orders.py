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
from utils import append_pagination_params, append_query_param, PaginationParams


@dataclass
class ListOpenOrdersRequest:
    portfolio: Optional[str] = None
    instrument: Optional[str] = None
    instrument_type: Optional[str] = None
    client_order_id: Optional[str] = None
    event_type: Optional[str] = None
    order_type: Optional[str] = None
    side: Optional[str] = None
    ref_datetime: Optional[str] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListOpenOrdersResponse(BaseResponse):
    request: ListOpenOrdersRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def list_open_orders(self, request: ListOpenOrdersRequest) -> ListOpenOrdersResponse:
        path = f"/orders"

        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, 'portfolio', request.portfolio)
        query_params = append_query_param(query_params, 'instrument', request.instrument)
        query_params = append_query_param(query_params, 'instrument_type', request.instrument_type)
        query_params = append_query_param(query_params, 'client_order_id', request.client_order_id)
        query_params = append_query_param(query_params, 'event_type', request.event_type)
        query_params = append_query_param(query_params, 'order_type', request.order_type)
        query_params = append_query_param(query_params, 'side', request.side)
        query_params = append_query_param(query_params, 'ref_datetime', request.ref_datetime)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListOpenOrdersResponse(response.json(), request)
