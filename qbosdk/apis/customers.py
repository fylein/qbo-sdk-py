"""
Quickbooks Online vendors
"""
from .api_base import ApiBase


class Customers(ApiBase):
    """Class for Customer APIs."""

    GET_CUSTOMERS = '/query?query=select * from Customer STARTPOSITION {0} MAXRESULTS 1000'
    COUNT_CUSTOMERS = '/query?query=select count(*) from Customer where Active = True'

    def get(self):
        """Get a list of the existing Customers in the Organization.

        Returns:
            List with dicts in Customers schema.
        """
        return self._query_get_all('Customer', Customers.GET_CUSTOMERS)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing Customers in the Organization.

        Returns:
            Generator with dicts in Customers schema.
        """
        if last_updated_time:
            Customers.GET_CUSTOMERS = Customers.GET_CUSTOMERS.replace(
                'from Customer',
                f"from Customer where MetaData.LastUpdatedTime > '{last_updated_time}'"
            )

        return self._query_get_all_generator('Customer', Customers.GET_CUSTOMERS)

    def count(self):
        """Get count of Customers in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Customers.COUNT_CUSTOMERS)['totalCount']

    def get_inactive(self, last_updated_time: None):
        """
        Retrieves a list of inactive customers from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the customers.
        :return: A list of inactive customers.
        """

        QUERY = "/query?query=select * from Customer where Active=false"
        if last_updated_time:
            QUERY += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        QUERY += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Customer', QUERY)
