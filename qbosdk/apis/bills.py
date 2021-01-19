"""
Quickbooks Online Bills
"""
from typing import Dict
from .api_base import ApiBase


class Bills(ApiBase):
    """Class for Bill APIs."""

    GET_BILLS = '/query?query=select * from Bill STARTPOSITION {0} MAXRESULTS 1000'
    POST_BILL = '/bill?minorversion=38'
    DELETE_BILL = '/bill?operation=delete'
    GET_BILL_BY_ID = '/bill/{0}'

    def get(self):
        """
        Get all Bills
        :return: List of Dicts in Bill Schema
        """
        return self._query_get_all('Bill', Bills.GET_BILLS)

    def post(self, data: Dict):
        """
        Post Bill to Quickbooks Online
        :param data: Dict in Bill schema
        :return:
        """
        return self._post_request(data, Bills.POST_BILL)

    def delete(self, bill_id: str):
        """
        Delete Bill from Quickbooks Online
        :param bill_id: Bill Id to remove
        :return: Dict response
        """
        data = {
            'Id': bill_id,
            'SyncToken': '1'
        }
        return self._post_request(data, Bills.DELETE_BILL)

    def get_by_id(self, bill_id):
        """
        Get Bill from Quickbooks Online
        :param bill_id: Bill Id
        :return: Dict Response
        """
        return self._get_request('Bill', Bills.GET_BILL_BY_ID.format(bill_id))
