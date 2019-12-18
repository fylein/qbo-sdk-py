"""
Quickbooks Online purchases
"""
from typing import Dict
from .api_base import ApiBase


class Purchases(ApiBase):
    """Class for Categories APIs."""

    GET_PURCHASES = '/query?query=select * from Purchase STARTPOSITION {0} MAXRESULTS 1000'
    POST_PURCHASE = '/purchase?minorversion=38'
    DELETE_PURCHASE = '/purchase?operation=delete'

    def get(self):
        """
        Get all Purchases
        :return: List of Dicts in Purchase Schema
        """
        return self._query_get_all('Purchase', Purchases.GET_PURCHASES)

    def post(self, data: Dict):
        """
        Post Purchase (check, etc) to Quickbooks Online
        :param data: Dict in Purchase schema
        :return:
        """
        return self._post_request(data, Purchases.POST_PURCHASE)

    def delete(self, purchase_id: str):
        """
        Delete Purchase (check, etc) from Quickbooks Online
        :param purchase_id: Journal Entry Id to remove
        :return: Dict response
        """
        data = {
            'Id': purchase_id,
            'SyncToken': '1'
        }
        return self._post_request(data, Purchases.DELETE_PURCHASE)
