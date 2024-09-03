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
from get_asset_details import IntxClient, GetAssetDetailsRequest, Credentials
from test_constants import (
    BASE_URL, CREDENTIALS_ENV, ASSET_NAME, PERP_NAME,
    ASSET_STATUS_ACTIVE, COLLATERAL_WEIGHT, ERROR_MESSAGE
)


class TestGetAssetDetails(unittest.TestCase):

    @patch('get_asset_details.Client')
    def test_get_asset_details_success(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "asset_name": ASSET_NAME,
            "status": ASSET_STATUS_ACTIVE,
            "collateral_weight": COLLATERAL_WEIGHT,
        }
        MockClient.return_value.request.return_value = mock_response

        credentials = Credentials.from_env(CREDENTIALS_ENV)
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = GetAssetDetailsRequest(asset=ASSET_NAME)
        response = intx_client.get_asset_details(request)

        self.assertEqual(response.response['asset_name'], ASSET_NAME)
        self.assertEqual(response.response['status'], ASSET_STATUS_ACTIVE)
        self.assertTrue(isinstance(response.response['collateral_weight'], float))

    @patch('get_asset_details.Client')
    def test_get_asset_details_failure(self, MockClient):
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception(ERROR_MESSAGE)

        MockClient.return_value.request.side_effect = mock_response.json.side_effect

        credentials = Credentials.from_env(CREDENTIALS_ENV)
        intx_client = IntxClient(credentials, base_url=BASE_URL)

        request = GetAssetDetailsRequest(asset=PERP_NAME)
        with self.assertRaises(Exception) as context:
            intx_client.get_asset_details(request)

        self.assertTrue(ERROR_MESSAGE in str(context.exception))


if __name__ == "__main__":
    unittest.main()
