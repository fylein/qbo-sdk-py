"""
Quickbooks Online vendors
"""
from .api_base import ApiBase


class Customers(ApiBase):
    """Class for Customer APIs."""

    GET_CUSTOMERS = '/query?query=select * from Customer STARTPOSITION {0} MAXRESULTS 1000'
    COUNT_CUSTOMERS = '/query?query=select count(*) from Customer'

    def get(self):
        """Get a list of the existing Customers in the Organization.

        Returns:
            List with dicts in Customers schema.
        """
        return self._query_get_all('Customer', Customers.GET_CUSTOMERS)

    def count(self):
        """Get count of Customers in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Customers.COUNT_CUSTOMERS)['totalCount']
