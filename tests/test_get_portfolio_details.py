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
from get_portfolio_details import IntxClient, GetPortfolioDetailsRequest, Credentials
from test_constants import BASE_URL


class TestGetPortfolioDetails(unittest.TestCase):

    @patch('get_portfolio_details.Client')
    def test_get_portfolio_details_success(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "portfolio_id": "dummy_portfolio_id",
            "name": "Test Portfolio",
            "status": "ACTIVE",
            "balance": "1000.00"
        }
        MockClient.return_value.request.return_value = mock_response

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = GetPortfolioDetailsRequest(portfolio="dummy_portfolio_id")
        response = intx_client.get_portfolio_details(request)

        self.assertEqual(response.response['portfolio_id'], "dummy_portfolio_id")
        self.assertEqual(response.response['name'], "Test Portfolio")
        self.assertEqual(response.response['status'], "ACTIVE")
        self.assertEqual(response.response['balance'], "1000.00")

    @patch('get_portfolio_details.Client')
    def test_get_portfolio_details_failure(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception("API error")

        MockClient.return_value.request.side_effect = mock_response.json.side_effect

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url="https://api-n5e1.coinbase.com/api/v1")

        request = GetPortfolioDetailsRequest(portfolio="dummy_portfolio_id")
        with self.assertRaises(Exception) as context:
            intx_client.get_portfolio_details(request)

        self.assertTrue('API error' in str(context.exception))


if __name__ == "__main__":
    unittest.main()
