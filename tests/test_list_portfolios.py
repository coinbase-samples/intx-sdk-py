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
from list_portfolios import IntxClient, ListPortfoliosRequest, Credentials
from test_constants import (
    BASE_URL, CREDENTIALS_ENV, DUMMY_PORTFOLIO_ID_1, DUMMY_PORTFOLIO_ID_2,
    DUMMY_PORTFOLIO_UUID_1, DUMMY_PORTFOLIO_UUID_2, DUMMY_PORTFOLIO_NAME_1,
    DUMMY_PORTFOLIO_NAME_2, USER_UUID_1, USER_UUID_2, FEE_RATE_ZERO,
    TAKER_FEE_RATE, BOOLEAN_FALSE, BOOLEAN_TRUE, ERROR_MESSAGE
)


class TestListPortfolios(unittest.TestCase):

    @patch('list_portfolios.Client')
    def test_list_portfolios_success(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "portfolio_id": DUMMY_PORTFOLIO_ID_1,
                "portfolio_uuid": DUMMY_PORTFOLIO_UUID_1,
                "name": DUMMY_PORTFOLIO_NAME_1,
                "user_uuid": USER_UUID_1,
                "maker_fee_rate": FEE_RATE_ZERO,
                "taker_fee_rate": TAKER_FEE_RATE,
                "trading_lock": BOOLEAN_FALSE,
                "withdrawal_lock": BOOLEAN_FALSE,
                "borrow_disabled": BOOLEAN_FALSE,
                "is_lsp": BOOLEAN_FALSE,
                "is_default": BOOLEAN_FALSE,
                "cross_collateral_enabled": BOOLEAN_FALSE,
                "auto_margin_enabled": BOOLEAN_FALSE,
                "pre_launch_trading_enabled": BOOLEAN_FALSE,
                "position_offsets_enabled": BOOLEAN_FALSE
            },
            {
                "portfolio_id": DUMMY_PORTFOLIO_ID_2,
                "portfolio_uuid": DUMMY_PORTFOLIO_UUID_2,
                "name": DUMMY_PORTFOLIO_NAME_2,
                "user_uuid": USER_UUID_2,
                "maker_fee_rate": FEE_RATE_ZERO,
                "taker_fee_rate": TAKER_FEE_RATE,
                "trading_lock": BOOLEAN_FALSE,
                "withdrawal_lock": BOOLEAN_FALSE,
                "borrow_disabled": BOOLEAN_FALSE,
                "is_lsp": BOOLEAN_FALSE,
                "is_default": BOOLEAN_TRUE,
                "cross_collateral_enabled": BOOLEAN_FALSE,
                "auto_margin_enabled": BOOLEAN_FALSE,
                "pre_launch_trading_enabled": BOOLEAN_FALSE,
                "position_offsets_enabled": BOOLEAN_FALSE
            }
        ]
        MockClient.return_value.request.return_value = mock_response

        credentials = Credentials.from_env(CREDENTIALS_ENV)
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = ListPortfoliosRequest()
        response = intx_client.list_portfolios(request)

        # Ensure response is a list
        self.assertIsInstance(response.response, list)

        # Ensure all items in the response are dictionaries
        self.assertTrue(all(isinstance(portfolio, dict) for portfolio in response.response))

        # Check specific fields in each portfolio
        self.assertTrue(all(isinstance(portfolio.get("portfolio_id"), str) for portfolio in response.response))
        self.assertTrue(all(isinstance(portfolio.get("is_default"), bool) for portfolio in response.response))

    @patch('list_portfolios.Client')
    def test_list_portfolios_failure(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception(ERROR_MESSAGE)

        MockClient.return_value.request.side_effect = mock_response.json.side_effect

        credentials = Credentials.from_env(CREDENTIALS_ENV)
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = ListPortfoliosRequest()
        with self.assertRaises(Exception) as context:
            intx_client.list_portfolios(request)

        self.assertIn(ERROR_MESSAGE, str(context.exception))


if __name__ == "__main__":
    unittest.main()
