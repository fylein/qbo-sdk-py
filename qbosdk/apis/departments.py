"""
Quickbooks Online departments
"""
from .api_base import ApiBase


class Departments(ApiBase):
    """Class for Categories APIs."""

    GET_DEPARTMENTS = '/query?query=select * from Department'
    COUNT_DEPARTMENT = '/query?query=select count(*) from Department where Active = True'

    def get(self):
        """Get a list of the existing Departments in the Organization.

        Returns:
            List with dicts in Departments schema.
        """
        QUERY = Departments.GET_DEPARTMENTS + " STARTPOSITION {0} MAXRESULTS 1000"
        return self._query_get_all('Department', QUERY)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing Departments in the Organization.

        Returns:
            Generator with dicts in Departments schema.
        """
        QUERY = Departments.GET_DEPARTMENTS
        if last_updated_time:
            QUERY += f" where Metadata.LastUpdatedTime >= '{last_updated_time}'"
        QUERY += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Department', QUERY)

    def get_inactive(self, last_updated_time: None):
        """
        Retrieves a list of inactive departments from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the departments.
        :return: A list of inactive departments.
        """

        QUERY = Departments.GET_DEPARTMENTS + " where Active=false"
        if last_updated_time:
            QUERY += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        QUERY += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Department', QUERY)

    def count(self):
        """Get count of Departments in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Departments.COUNT_DEPARTMENT)['totalCount']
