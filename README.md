# QuickbooksOnlineSDK

Python SDK for accessing QBO APIs.

## Installation

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. Install it from [pip](https://pypi.org).
        
        $ pip install qbosdk

## Usage

To use this SDK you'll need these QBO credentials used for OAuth2 authentication: **client ID**, **client secret** and **refresh token**.

This SDK is very easy to use.
1. First you'll need to create a connection using the main class QuickbooksOnlineSDK.
```python
from qbosdk import QuickbooksOnlineSDK

connection = QuickbooksOnlineSDK(
    client_id='<YOUR CLIENT ID>',
    client_secret='<YOUR CLIENT SECRET>',
    refresh_token='<YOUR REFRESH TOKEN>',
    realm_id='<REALM / COMPANY ID>',
    environment='<sandbox / production>'
)
```
2. After that you'll be able to access any of the API classes
```python
"""
USAGE: <QuickbooksOnlineSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""

# Get a list of all Employees (with all available details for Employee)
response = connection.employees.get()

# Get a list of all Accounts
response = connection.accounts.get()
```

See more details about the usage into the wiki pages of this project.

## Integration Tests

To run integration tests, you will need a mechanism to connect to a real qbo account. Save this info in a test_credentials.json file in your root directory:

```json
{
  "client_id": "<client_id>",
  "client_secret": "<client_secret>",
  "realm_id": "<realm_id>",
  "refresh_token": "<refresh_token>",
  "environment": "<environment sandbox / production>"
}
```

```bash
$ pip install pytest

$ python -m pytest test/integration
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
