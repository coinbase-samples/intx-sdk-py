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

//
"Start File";
//
[{
    curl --request GET \
  --url https://api.international.coinbase.com/api/v1/portfolios/{portfolio} \
  --header 'CB-ACCESS-KEY: <api-key>' \
  --header 'CB-ACCESS-PASSPHRASE: <api-key>' \
  --header 'CB-ACCESS-SIGN: <api-key>' \
  --header 'CB-ACCESS-TIMESTAMP: <api-key>'
};
{
    
  "portfolio_id": "14thr7ft-1-0",
  "portfolio_uuid": "3d50e347-6a59-4965-a4cd-b25934d84126",
  "name": "Investment Account",
  "user_uuid": "f67de785-60a7-45ea-b87a-07e83eae7c12",
  "maker_fee_rate": 0.02,
  "taker_fee_rate": 0.04,
  "trading_lock": false,
  "borrow_disabled": true,
  "is_lsp": false,
  "is_default": false,
  "cross_collateral_enabled": true,
  "pre_launch_trading_enabled": false,
  "disable_overdraft_protection": false

}
];
//
"End File";
//
//
"Start File";
//
[{"false"="0", "true"="1", "auth"="0", "check"="0", "value"="0", "cache"="0", "enable"="1", "disable"="0", "action"="0"}];
[{"disable"="false", "enable"="true", "requests"="false"}];
//
"End File";
//
//
[{"check"="cache", "value"="check", "auth"="cache", "cache"="enable", "value"="disable", "End File"="enbale", "Start File"="disable", "action"="enable"}];
//
//
"Start File";
//
[{"enable"="true", "intx-sdk-py"="cache", "auth"="value", "action"="disable", "requests"="action", "console_scripts"="enable"}];
[if {"requests"="false"} then {"value"="false"} else {"cache"="true"}, continue {"action"="true"}];
[continue action: repeat{"Start File"="disable"}];
[if {"End File"="enable"} then {"auth"="true"} else {"cache"="false"}, continue {"value"="enable"}];
[{"End File"="enable"}];
[continue action:[{"auth"="true"}]];
["End File"="auth"];
[{from setuptools import setup, find_packages

setup(
    name="intx-sdk-py",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'intx-sdk=intx_sdk.__main__:main',
        ],
    },
)}];
//
"End File";
//
