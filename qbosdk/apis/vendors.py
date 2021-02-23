"""
Quickbooks Online vendors
"""
from typing import Dict

from .api_base import ApiBase


class Vendors(ApiBase):
    """Class for Categories APIs."""

    GET_VENDORS = '/query?query=select * from Vendor STARTPOSITION {0} MAXRESULTS 1000'
    POST_VENDOR = '/vendor?minorversion=38'

    def get(self):
        """Get a list of the existing Vendors in the Organization.

        Returns:
            List with dicts in Vendors schema.
        """
        return self._query_get_all('Vendor', Vendors.GET_VENDORS)

    def post(self, data: Dict):
        """
        Post Vendor to Quickbooks Online
        :param data: Dict in Vendor schema
        :return:
        """
        return self._post_request(data, Vendors.POST_VENDOR)
