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

import unittest
from unittest.mock import patch, MagicMock
from list_portfolios import IntxClient, ListPortfoliosRequest, Credentials
from test_constants import BASE_URL


class TestListPortfolios(unittest.TestCase):

    @patch('list_portfolios.Client')
    def test_list_portfolios_success(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "portfolio_id": "dummy_id_1",
                "portfolio_uuid": "dummy_uuid_1",
                "name": "dummy_portfolio_1",
                "user_uuid": "dummy_user_uuid_1",
                "maker_fee_rate": "0",
                "taker_fee_rate": "0.0002",
                "trading_lock": False,
                "withdrawal_lock": False,
                "borrow_disabled": False,
                "is_lsp": False,
                "is_default": False,
                "cross_collateral_enabled": False,
                "auto_margin_enabled": False,
                "pre_launch_trading_enabled": False,
                "position_offsets_enabled": False
            },
            {
                "portfolio_id": "dummy_id_2",
                "portfolio_uuid": "dummy_uuid_2",
                "name": "dummy_portfolio_2",
                "user_uuid": "dummy_user_uuid_2",
                "maker_fee_rate": "0",
                "taker_fee_rate": "0.0002",
                "trading_lock": False,
                "withdrawal_lock": False,
                "borrow_disabled": False,
                "is_lsp": False,
                "is_default": True,
                "cross_collateral_enabled": False,
                "auto_margin_enabled": False,
                "pre_launch_trading_enabled": False,
                "position_offsets_enabled": False
            }
        ]
        MockClient.return_value.request.return_value = mock_response

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = ListPortfoliosRequest()
        response = intx_client.list_portfolios(request)

        self.assertEqual(len(response.response), 2)
        self.assertTrue(all(isinstance(portfolio["portfolio_id"], str) for portfolio in response.response))
        self.assertTrue(all(isinstance(portfolio["is_default"], bool) for portfolio in response.response))

    @patch('list_portfolios.Client')
    def test_list_portfolios_failure(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception("API error")

        MockClient.return_value.request.side_effect = mock_response.json.side_effect

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url="https://api-n5e1.coinbase.com/api/v1")

        request = ListPortfoliosRequest()
        with self.assertRaises(Exception) as context:
            intx_client.list_portfolios(request)

        self.assertTrue('API error' in str(context.exception))


if __name__ == "__main__":
    unittest.main()
