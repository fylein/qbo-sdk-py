"""
Quickbooks Online employees
"""

from .api_base import ApiBase


class Items(ApiBase):
    """Class for Items APIs."""

    GET_ITEMS = '/query?query=select * from Item STARTPOSITION {0} MAXRESULTS 1000'

    def get(self):
        """Get a list of the existing items in the Organization.

        Returns:
            List with dicts in Items schema.
        """
        return self._query_get_all('Item', Items.GET_ITEMS)
