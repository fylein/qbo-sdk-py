"""
Quickbooks Online classes
"""
from .api_base import ApiBase


class Classes(ApiBase):
    """Class for Categories APIs."""

    GET_CLASSES = '/query?query=select * from Class STARTPOSITION {0} MAXRESULTS 1000'
    COUNT_CLASSES = '/query?query=select count(*) from Class where Active = True'

    def get(self):
        """Get a list of the existing Classes in the Organization.

        Returns:
            List with dicts in Classes schema.
        """
        return self._query_get_all('Class', Classes.GET_CLASSES)

    def get_all_generator(self):
        """Get a list of the existing Classes in the Organization.

        Returns:
            Generator with dicts in Classes schema.
        """
        return self._query_get_all_generator('Class', Classes.GET_CLASSES)


    def count(self):
        """Get count of Classes in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Classes.COUNT_CLASSES)['totalCount']
