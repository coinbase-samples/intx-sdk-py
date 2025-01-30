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
class PatchPortfolioRequest:
    portfolio_name: str
    auto_margin_enabled: Optional[str] = None
    cross_collateral_enabled: Optional[str] = None
    position_offsets_enabled: Optional[str] = None
    pre_launch_trading_enabled: Optional[str] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class PatchPortfolioResponse(BaseResponse):
    request: PatchPortfolioRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def patch_portfolio(self, request: PatchPortfolioRequest) -> PatchPortfolioResponse:
        path = f"/portfolios/{request.portfolio_name}"
        body = {k: v for k, v in asdict(request).items() if v is not None and k != "portfolio_name"}
        response = self.client.request("PATCH", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return PatchPortfolioResponse(response.json(), request)
