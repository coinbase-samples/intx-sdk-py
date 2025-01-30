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


@dataclass
class GetQuotePerInstrumentRequest:
    instrument: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetQuotePerInstrumentResponse(BaseResponse):
    request: GetQuotePerInstrumentRequest


class IntxClient:
    def __init__(self, credentials: Credentials, base_url: Optional[str] = None):
        self.client = Client(credentials, base_url=base_url)

    def get_quote_per_instrument(self, request: GetQuotePerInstrumentRequest) -> GetQuotePerInstrumentResponse:
        path = f"/instruments/{request.instrument}/quote"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetQuotePerInstrumentResponse(response.json(), request)
