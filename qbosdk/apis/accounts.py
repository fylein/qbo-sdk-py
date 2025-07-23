"""
Quickbooks Online accounts
"""
from .api_base import ApiBase


class Accounts(ApiBase):
    """Class for Categories APIs."""

    GET_ACCOUNTS = '/query?query=select * from Account'
    ACCOUNT_COUNT = '/query?query=select count(*) from Account where Active = True'

    def get(self):
        """Get a list of the existing Accounts in the Organization.

        Returns:
            List with dicts in Accounts schema.
        """
        query = Accounts.GET_ACCOUNTS + " STARTPOSITION {0} MAXRESULTS 1000"
        return self._query_get_all('Account', query)

    def get_all_generator(self, last_updated_time = None):
        """Get a generator of all the existing Accounts in the Organization.

        Returns:
            Generator with dicts in Accounts schema.
        """
        query = Accounts.GET_ACCOUNTS
        if last_updated_time:
            query += f" where Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Account', query)

    def get_inactive(self, last_updated_time: None):
        """
        Retrieves a list of inactive accounts from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the accounts.
        :return: A list of inactive accounts.
        """

        query = Accounts.GET_ACCOUNTS + " where Active=false"
        if last_updated_time:
            query += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Account', query)

    def count(self):
        """Get count of Accounts in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Accounts.ACCOUNT_COUNT)['totalCount']
