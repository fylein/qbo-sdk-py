"""
Quickbooks Online vendors
"""
from .api_base import ApiBase


class Customers(ApiBase):
    """Class for Customer APIs."""

    GET_CUSTOMERS = '/query?query=select * from Customer STARTPOSITION {0} MAXRESULTS 1000'

    def get(self):
        """Get a list of the existing Customers in the Organization.

        Returns:
            List with dicts in Customers schema.
        """
        return self._query_get_all('Customer', Customers.GET_CUSTOMERS)
