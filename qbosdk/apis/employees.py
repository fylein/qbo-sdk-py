"""
Quickbooks Online employees
"""
from typing import Dict

from .api_base import ApiBase


class Employees(ApiBase):
    """Class for Categories APIs."""

    GET_EMPLOYEES = '/query?query=select * from Employee STARTPOSITION {0} MAXRESULTS 1000'
    POST_EMPLOYEE = '/employee?minorversion=38'
    COUNT_EMPLOYEES = '/query?query=select count(*) from Employee where Active = True'

    def get(self):
        """Get a list of the existing Employees in the Organization.

        Returns:
            List with dicts in Employees schema.
        """
        return self._query_get_all('Employee', Employees.GET_EMPLOYEES)

    def get_all_generator(self):
        """Get a list of the existing Employees in the Organization.

        Returns:
            Generator with dicts in Employees schema.
        """
        return self._query_get_all_generator('Employee', Employees.GET_EMPLOYEES)

    def post(self, data: Dict):
        """
        Post Employee to Quickbooks Online
        :param data: Dict in Employee schema
        :return:
        """
        return self._post_request(data, Employees.POST_EMPLOYEE)

    def count(self):
        """Get count of Employees in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Employees.COUNT_EMPLOYEES)['totalCount']

