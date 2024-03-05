"""
Quickbooks Online accounts
"""
from .api_base import ApiBase


class Accounts(ApiBase):
    """Class for Categories APIs."""

    GET_ACCOUNTS = '/query?query=select * from Account STARTPOSITION {0} MAXRESULTS 1000'

    def get(self):
        """Get a list of the existing Accounts in the Organization.

        Returns:
            List with dicts in Accounts schema.
        """
        return self._query_get_all('Account', Accounts.GET_ACCOUNTS)

    def get_all_generator(self):
        """Get a generator of all the existing Accounts in the Organization.

        Returns:
            Generator with dicts in Accounts schema.
        """
        return self._query_get_all_generator('Account', Accounts.GET_ACCOUNTS)

    def get_inactive(self, last_updated_time):
        """
        Retrieves a list of inactive accounts from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the accounts.
        :return: A list of inactive accounts.
        """

        QUERY = "/query?query=select * from Account where Active=false"
        if last_updated_time:
            QUERY += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        QUERY += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Account', QUERY)
