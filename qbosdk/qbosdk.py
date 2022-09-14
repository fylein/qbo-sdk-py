"""
Quickbooks online Python SDK
"""
import json
import base64
import requests
from future.moves.urllib.parse import urlencode

from .exceptions import *
from .apis import *


class QuickbooksOnlineSDK:
    """
    Quickbooks Online SDK
    """
    TOKEN_URL = 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'
    TOKEN_REVOKE_URL = 'https://developer.API.intuit.com/v2/oauth2/tokens/revoke'

    def __init__(self, client_id: str, client_secret: str,
                 refresh_token: str, realm_id: str, environment: str):
        """
        Initialize connection to Quickbooks Online
        :param client_id: Quickbooks online client_Id
        :param client_secret: Quickbooks online client_secret
        :param refresh_token: Quickbooks online refresh_token
        :param realm_id: Quickbooks onliine realm / company id
        :param environment: production or sandbox
        """
        # Initializing variables
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.refresh_token = refresh_token
        self.__realm_id = realm_id

        if environment.lower() == 'production':
            self.__base_url = 'https://quickbooks.api.intuit.com/v3/company/{0}'.format(self.__realm_id)
            self.web_app_url = 'https://app.qbo.intuit.com'
        elif environment.lower() == 'sandbox':
            self.__base_url = 'https://sandbox-quickbooks.api.intuit.com/v3/company/{0}'.format(self.__realm_id)
            self.web_app_url = 'https://app.sandbox.qbo.intuit.com'
        else:
            raise ValueError('environment can only be prodcution / sandbox')

        self.__access_token = None

        self.accounts = Accounts()
        self.departments = Departments()
        self.customers = Customers()
        self.classes = Classes()
        self.vendors = Vendors()
        self.employees = Employees()
        self.preferences = Preferences()
        self.company_info = CompanyInfo(self.__realm_id)
        self.exchange_rates = ExchangeRates()
        self.bills = Bills()
        self.purchases = Purchases()
        self.journal_entries = JournalEntries()
        self.attachments = Attachments()
        self.bill_payments = BillPayments()
        self.tax_codes = TaxCodes()
        self.tax_rates = TaxRates()

        self.update_server_url()
        self.update_access_token()

    def update_server_url(self):
        """
        Update the server url in all API objects.
        """
        base_url = self.__base_url

        self.accounts.set_server_url(base_url)
        self.departments.set_server_url(base_url)
        self.classes.set_server_url(base_url)
        self.vendors.set_server_url(base_url)
        self.employees.set_server_url(base_url)
        self.preferences.set_server_url(base_url)
        self.company_info.set_server_url(base_url)
        self.exchange_rates.set_server_url(base_url)
        self.bills.set_server_url(base_url)
        self.purchases.set_server_url(base_url)
        self.journal_entries.set_server_url(base_url)
        self.customers.set_server_url(base_url)
        self.attachments.set_server_url(base_url)
        self.bill_payments.set_server_url(base_url)
        self.tax_codes.set_server_url(base_url)
        self.tax_rates.set_server_url(base_url)

    def update_access_token(self):
        """
        Update the access token and change it in all API objects.
        """
        self.__get_access_token()
        access_token = self.__access_token

        self.accounts.change_access_token(access_token)
        self.departments.change_access_token(access_token)
        self.classes.change_access_token(access_token)
        self.vendors.change_access_token(access_token)
        self.employees.change_access_token(access_token)
        self.preferences.change_access_token(access_token)
        self.company_info.change_access_token(access_token)
        self.exchange_rates.change_access_token(access_token)
        self.bills.change_access_token(access_token)
        self.purchases.change_access_token(access_token)
        self.journal_entries.change_access_token(access_token)
        self.customers.change_access_token(access_token)
        self.attachments.change_access_token(access_token)
        self.bill_payments.change_access_token(access_token)
        self.tax_codes.change_access_token(access_token)
        self.tax_rates.change_access_token(access_token)

    def __get_access_token(self):
        """Get the access token using a HTTP post.

        Returns:
            A new access token.
        """

        api_data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }

        auth = '{0}:{1}'.format(self.__client_id, self.__client_secret)
        auth = base64.b64encode(auth.encode('utf-8'))

        request_header = {
            'Accept': 'application/json',
            'Content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic {0}'.format(
                str(auth.decode())
            )
        }

        token_url = QuickbooksOnlineSDK.TOKEN_URL.format(self.__base_url)
        response = requests.post(url=token_url, data=urlencode(api_data), headers=request_header)

        if response.status_code == 200:
            auth = json.loads(response.text)
            self.__access_token = auth['access_token']
            self.refresh_token = auth['refresh_token']

        elif response.status_code == 400:
            raise WrongParamsError('Something wrong with the request body', response.text)

        elif response.status_code == 401:
            raise UnauthorizedClientError('Wrong client secret or/and refresh token', response.text)

        elif response.status_code == 404:
            raise NotFoundClientError('Client ID doesn\'t exist', response.text)

        elif response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        else:
            raise QuickbooksOnlineSDKError('Error: {0}'.format(response.status_code), response.text)

def revoke_refresh_token(refresh_token: str, client_id: str, client_secret: str):
    api_data = {
        'token': refresh_token
    }

    auth = '{0}:{1}'.format(client_id, client_secret)
    auth = base64.b64encode(auth.encode('utf-8'))

    request_header = {
        'Accept': 'application/json',
        'Content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {0}'.format(
            str(auth.decode())
        )
    }

    response = requests.post(url=QuickbooksOnlineSDK.TOKEN_REVOKE_URL, data=api_data, headers=request_header)

    if response.status_code == 200:
        return {'message': 'Token revoked successfully'}

    else:
        raise QuickbooksOnlineSDKError('Error: {0}'.format(response.status_code), response.text)
