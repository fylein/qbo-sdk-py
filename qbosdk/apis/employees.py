"""
Quickbooks Online employees
"""
from .api_base import ApiBase


class Employees(ApiBase):
    """Class for Categories APIs."""

    GET_EMPLOYEES = '/query?query=select * from Employee STARTPOSITION {0} MAXRESULTS 1000'

    def get(self):
        """Get a list of the existing Employees in the Organization.

        Returns:
            List with dicts in Employees schema.
        """
        return self._query_get_all('Employee', Employees.GET_EMPLOYEES)
