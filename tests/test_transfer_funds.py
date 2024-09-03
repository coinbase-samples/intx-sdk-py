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
from transfer_funds import IntxClient, TransferFundsRequest, Credentials
from test_constants import (
    BASE_URL, CREDENTIALS_ENV, TRANSACTION_ID, TRANSFER_STATUS_COMPLETED,
    FROM_PORTFOLIO, TO_PORTFOLIO, ASSET_NAME_BTC, TRANSFER_AMOUNT, ERROR_MESSAGE
)


class TestTransferFunds(unittest.TestCase):

    @patch('transfer_funds.Client')
    def test_transfer_funds_success(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "transaction_id": TRANSACTION_ID,
            "status": TRANSFER_STATUS_COMPLETED,
            "from_portfolio": FROM_PORTFOLIO,
            "to_portfolio": TO_PORTFOLIO,
            "asset": ASSET_NAME_BTC,
            "amount": TRANSFER_AMOUNT
        }
        MockClient.return_value.request.return_value = mock_response

        credentials = Credentials.from_env(CREDENTIALS_ENV)
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = TransferFundsRequest(
            from_portfolio=FROM_PORTFOLIO,
            to_portfolio=TO_PORTFOLIO,
            asset=ASSET_NAME_BTC,
            amount=TRANSFER_AMOUNT
        )
        response = intx_client.transfer_funds(request)

        self.assertEqual(response.response['transaction_id'], TRANSACTION_ID)
        self.assertEqual(response.response['status'], TRANSFER_STATUS_COMPLETED)
        self.assertEqual(response.response['from_portfolio'], FROM_PORTFOLIO)
        self.assertEqual(response.response['to_portfolio'], TO_PORTFOLIO)
        self.assertEqual(response.response['asset'], ASSET_NAME_BTC)
        self.assertEqual(response.response['amount'], TRANSFER_AMOUNT)

    @patch('transfer_funds.Client')
    def test_transfer_funds_failure(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception(ERROR_MESSAGE)

        MockClient.return_value.request.side_effect = mock_response.json.side_effect

        credentials = Credentials.from_env(CREDENTIALS_ENV)
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = TransferFundsRequest(
            from_portfolio=FROM_PORTFOLIO,
            to_portfolio=TO_PORTFOLIO,
            asset=ASSET_NAME_BTC,
            amount=TRANSFER_AMOUNT
        )
        with self.assertRaises(Exception) as context:
            intx_client.transfer_funds(request)

        self.assertIn(ERROR_MESSAGE, str(context.exception))


if __name__ == "__main__":
    unittest.main()
