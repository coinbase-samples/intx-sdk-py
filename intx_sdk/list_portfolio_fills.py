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
class ListPortfolioFillsRequest:
    portfolio: str
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None
    order_id: Optional[str] = None
    client_order_id: Optional[str] = None
    ref_datetime: Optional[str] = None
    time_from: Optional[str] = None


@dataclass
class ListPortfolioFillsResponse(BaseResponse):
    request: ListPortfolioFillsRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def list_portfolio_fills(self, request: ListPortfolioFillsRequest) -> ListPortfolioFillsResponse:
        path = f"/portfolios/{request.portfolio}/fills"

        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, 'portfolio', request.portfolio)
        query_params = append_query_param(query_params, 'order_id', request.order_id)
        query_params = append_query_param(query_params, 'client_order_id', request.client_order_id)
        query_params = append_query_param(query_params, 'ref_datetime', request.ref_datetime)
        query_params = append_query_param(query_params, 'time_from', request.time_from)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioFillsResponse(response.json(), request)
