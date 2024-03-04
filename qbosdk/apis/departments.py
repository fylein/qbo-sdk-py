"""
Quickbooks Online departments
"""
from .api_base import ApiBase


class Departments(ApiBase):
    """Class for Categories APIs."""

    GET_DEPARTMENTS = '/query?query=select * from Department STARTPOSITION {0} MAXRESULTS 1000'

    def get(self):
        """Get a list of the existing Departments in the Organization.

        Returns:
            List with dicts in Departments schema.
        """
        return self._query_get_all('Department', Departments.GET_DEPARTMENTS)

    def get_all_generator(self):
        """Get a list of the existing Departments in the Organization.

        Returns:
            Generator with dicts in Departments schema.
        """
        return self._query_get_all_generator('Department', Departments.GET_DEPARTMENTS)
