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
from transfer_funds import IntxClient, TransferFundsRequest, Credentials
from test_constants import BASE_URL


class TestTransferFunds(unittest.TestCase):

    @patch('transfer_funds.Client')
    def test_transfer_funds_success(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "transaction_id": "dummy_transaction_id",
            "status": "COMPLETED",
            "from_portfolio": "portfolio_1",
            "to_portfolio": "portfolio_2",
            "asset": "BTC",
            "amount": "0.5"
        }
        MockClient.return_value.request.return_value = mock_response

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = TransferFundsRequest(
            from_portfolio="portfolio_1",
            to_portfolio="portfolio_2",
            asset="BTC",
            amount="0.5"
        )
        response = intx_client.transfer_funds(request)

        self.assertEqual(response.response['transaction_id'], "dummy_transaction_id")
        self.assertEqual(response.response['status'], "COMPLETED")
        self.assertEqual(response.response['from_portfolio'], "portfolio_1")
        self.assertEqual(response.response['to_portfolio'], "portfolio_2")
        self.assertEqual(response.response['asset'], "BTC")
        self.assertEqual(response.response['amount'], "0.5")

    @patch('transfer_funds.Client')
    def test_transfer_funds_failure(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception("API error")

        MockClient.return_value.request.side_effect = mock_response.json.side_effect

        credentials = Credentials.from_env("INTX_CREDENTIALS")
        intx_client = IntxClient(credentials, base_url="https://api-n5e1.coinbase.com/api/v1")

        request = TransferFundsRequest(
            from_portfolio="portfolio_1",
            to_portfolio="portfolio_2",
            asset="BTC",
            amount="0.5"
        )
        with self.assertRaises(Exception) as context:
            intx_client.transfer_funds(request)

        self.assertTrue('API error' in str(context.exception))


if __name__ == "__main__":
    unittest.main()
