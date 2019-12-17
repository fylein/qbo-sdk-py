from typing import Dict
from .api_base import ApiBase


class Purchases(ApiBase):
    """Class for Categories APIs."""

    GET_PURCHASES = '/query?query=select * from Purchase STARTPOSITION {0} MAXRESULTS 1000'
    POST_PURCHASE = '/purchase?minorversion=38'

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
