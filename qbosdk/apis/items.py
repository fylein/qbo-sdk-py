"""
Quickbooks Online employees
"""

from .api_base import ApiBase


class Items(ApiBase):
    """Class for Items APIs."""

    GET_ITEMS = '/query?query=select * from Item STARTPOSITION {0} MAXRESULTS 1000'
    COUNT_ITEMS = '/query?query=select count(*) from Item where Active = True'

    def get(self):
        """Get a list of the existing items in the Organization.

        Returns:
            List with dicts in Items schema.
        """
        return self._query_get_all('Item', Items.GET_ITEMS)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing items in the Organization.

        Returns:
            Generator with dicts in Items schema.
        """
        if last_updated_time:
            Items.GET_ITEMS = Items.GET_ITEMS.replace(
                'from Item',
                f"from Item where MetaData.LastUpdatedTime > '{last_updated_time}'"
            )

        return self._query_get_all_generator('Item', Items.GET_ITEMS)

    def get_inactive(self, last_updated_time: None):
        """
        Retrieves a list of inactive items from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the items.
        :return: A list of inactive items.
        """

        QUERY = "/query?query=select * from Item where Active=false"
        if last_updated_time:
            QUERY += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        QUERY += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Item', QUERY)

    def count(self):
        """Get count of Items in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Items.COUNT_ITEMS)['totalCount']
