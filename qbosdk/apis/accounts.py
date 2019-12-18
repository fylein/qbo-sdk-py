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
