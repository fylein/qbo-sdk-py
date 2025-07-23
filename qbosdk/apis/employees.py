"""
Quickbooks Online employees
"""
from typing import Dict

from .api_base import ApiBase


class Employees(ApiBase):
    """Class for Categories APIs."""

    GET_EMPLOYEES = '/query?query=select * from Employee'
    POST_EMPLOYEE = '/employee'
    COUNT_EMPLOYEES = '/query?query=select count(*) from Employee where Active = True'

    def get(self):
        """Get a list of the existing Employees in the Organization.

        Returns:
            List with dicts in Employees schema.
        """
        query = Employees.GET_EMPLOYEES + " STARTPOSITION {0} MAXRESULTS 1000"
        return self._query_get_all('Employee', query)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing Employees in the Organization.

        Returns:
            Generator with dicts in Employees schema.
        """
        query = Employees.GET_EMPLOYEES
        if last_updated_time:
            query += f" where Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Employee', query)

    def get_inactive(self, last_updated_time: None):
        """
        Retrieves a list of inactive employees from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the employees.
        :return: A list of inactive employees.
        """
        query = Employees.GET_EMPLOYEES + " where Active=false"
        if last_updated_time:
            query += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"
        return self._query_get_all_generator('Employee', query)

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
