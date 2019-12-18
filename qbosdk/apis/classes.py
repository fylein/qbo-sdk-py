"""
Quickbooks Online classes
"""
from .api_base import ApiBase


class Classes(ApiBase):
    """Class for Categories APIs."""

    GET_CLASSES = '/query?query=select * from Class STARTPOSITION {0} MAXRESULTS 1000'

    def get(self):
        """Get a list of the existing Classes in the Organization.

        Returns:
            List with dicts in Classes schema.
        """
        return self._query_get_all('Class', Classes.GET_CLASSES)
