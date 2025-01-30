# International Exchange (INTX) Python SDK README

## Overview

The *INTX Python SDK* is a sample library that demonstrates the usage of the [Coinbase International Exchange (INTX)](https://international.coinbase.com/) API via its [REST APIs](https://docs.cdp.coinbase.com/intx/reference). This SDK provides a structured way to integrate Coinbase INTX functionalities into your Python applications.

## License

The *INTX Python SDK* sample library is free and open source and released under the [Apache License, Version 2.0](LICENSE).

The application and code are only available for demonstration purposes.

## Usage

### Setting Up Credentials

To use the *INTX Python SDK*, initialize the [Credentials](intx_sdk/credentials.py) class with your INTX API credentials. This class is designed to facilitate the secure handling of sensitive information required to authenticate API requests.

Ensure that your API credentials are stored securely and are not hard-coded directly in your source code. The Credentials class supports creating credentials from a JSON string or directly from environment variables, providing flexibility and enhancing security.

#### Example Initialization:

```python
from intx_sdk.credentials import Credentials

credentials = Credentials.from_env("INTX_CREDENTIALS")
```

#### Specifying the base url
INTX supports both production and sandbox environments. You can specify the desired environment by setting the base URL when initializing the `IntxClient`:
```python
intx_client = IntxClient(credentials, base_url="https://api-n5e1.coinbase.com/api/v1")
```
If no `base_url` is provided, the default production URL will be used.

#### Environment Variable Format: 

The JSON format expected for `INTX_CREDENTIALS` is:

```
{
  "accessKey": "",
  "passphrase": "",
  "signingKey": "",
}
```

### Obtaining API Credentials 

Coinbase INTX API credentials can be created in the INTX web console under Settings -> APIs. 

### Making API Calls
Once the client is initialized, make the desired call. For example, to [list portfolios](intx_sdk/list_portfolios.py),
pass in the request object, check for an error, and if nil, process the response.

```python
from intx_sdk.list_portfolios import IntxClient, ListPortfoliosRequest

credentials = Credentials.from_env("INTX_CREDENTIALS")
intx_client = IntxClient(credentials)

request = ListPortfoliosRequest()
try:
    response = intx_client.list_portfolios(request)
    print(response)
except Exception as e:
    print(f"failed to list portfolios: {e}")
```

### Supported Versions
The SDK is tested and confirmed to work with Python version 3.8 and newer.

### Specifying Binaries (Version 0.2.0)
To use version 0.2.0 of the INTX Python SDK, you can install the specific binary using pip:
```
pip install intx-sdk-py==0.2.0
```
Ensure that you are using the correct version to match the SDK capabilities and features described in this document.

