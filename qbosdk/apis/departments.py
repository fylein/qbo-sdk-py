"""
Quickbooks Online departments
"""
from .api_base import ApiBase


class Departments(ApiBase):
    """Class for Categories APIs."""

    GET_DEPARTMENTS = '/query?query=select * from Department STARTPOSITION {0} MAXRESULTS 1000'
    COUNT_DEPARTMENT = '/query?query=select count(*) from Department where Active = True'

    def get(self):
        """Get a list of the existing Departments in the Organization.

        Returns:
            List with dicts in Departments schema.
        """
        return self._query_get_all('Department', Departments.GET_DEPARTMENTS)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing Departments in the Organization.

        Returns:
            Generator with dicts in Departments schema.
        """
        if last_updated_time:
            Departments.GET_DEPARTMENTS = Departments.GET_DEPARTMENTS.replace(
                'from Department',
                f"from Department where MetaData.LastUpdatedTime > '{last_updated_time}'"
            )

        return self._query_get_all_generator('Department', Departments.GET_DEPARTMENTS)

    def count(self):
        """Get count of Departments in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Departments.COUNT_DEPARTMENT)['totalCount']
