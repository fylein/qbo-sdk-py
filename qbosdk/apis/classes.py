"""
Quickbooks Online classes
"""
from .api_base import ApiBase


class Classes(ApiBase):
    """Class for Categories APIs."""

    GET_CLASSES = '/query?query=select * from Class'
    COUNT_CLASSES = '/query?query=select count(*) from Class where Active = True'

    def get(self):
        """Get a list of the existing Classes in the Organization.

        Returns:
            List with dicts in Classes schema.
        """
        query = Classes.GET_CLASSES + " STARTPOSITION {0} MAXRESULTS 1000"
        return self._query_get_all('Class', query)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing Classes in the Organization.

        Returns:
            Generator with dicts in Classes schema.
        """
        query = Classes.GET_CLASSES
        if last_updated_time:
            query += f" where Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Class', query)


    def get_inactive(self, last_updated_time: None):
        """
        Retrieves a list of inactive classes from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the classes.
        :return: A list of inactive classes.
        """

        query = Classes.GET_CLASSES + " where Active=false"
        if last_updated_time:
            query += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Class', query)


    def count(self):
        """Get count of Classes in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Classes.COUNT_CLASSES)['totalCount']
