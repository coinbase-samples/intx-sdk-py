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
# limitations under the License.

import unittest
from unittest.mock import patch, MagicMock
from get_balance_for_portfolio_asset import IntxClient, GetBalanceForPortfolioAssetRequest, Credentials
from test_constants import BASE_URL


class TestGetBalanceForPortfolioAsset(unittest.TestCase):

    @patch('get_balance_for_portfolio_asset.Client')
    def test_get_balance_for_portfolio_asset_success(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "portfolio_id": "dummy_portfolio_id",
            "asset": "BTC",
            "balance": "1.5"
        }
        MockClient.return_value.request.return_value = mock_response

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = GetBalanceForPortfolioAssetRequest(portfolio="dummy_portfolio_id", asset="BTC")
        response = intx_client.get_balance_for_portfolio_asset(request)

        self.assertEqual(response.response['portfolio_id'], "dummy_portfolio_id")
        self.assertEqual(response.response['asset'], "BTC")
        self.assertEqual(response.response['balance'], "1.5")

    @patch('get_balance_for_portfolio_asset.Client')
    def test_get_balance_for_portfolio_asset_failure(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception("API error")

        MockClient.return_value.request.side_effect = mock_response.json.side_effect

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url="https://api-n5e1.coinbase.com/api/v1")

        request = GetBalanceForPortfolioAssetRequest(portfolio="dummy_portfolio_id", asset="BTC")
        with self.assertRaises(Exception) as context:
            intx_client.get_balance_for_portfolio_asset(request)

        self.assertTrue('API error' in str(context.exception))


if __name__ == "__main__":
    unittest.main()