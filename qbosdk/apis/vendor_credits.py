"""
Quickbooks Online vendor credits
"""
from typing import Dict

from .api_base import ApiBase


class VendorCredits(ApiBase):
    """Class for VendorCredits APIs."""

    GET_VENDORS = '/query?query=select * from vendorcredit STARTPOSITION {0} MAXRESULTS 1000'
    POST_VENDOR = '/vendorcredit?minorversion=62'

    def get(self):
        """Get a list of the existing VendorCredits in the Organization.

        Returns:
            List with dicts in VendorCredits schema.
        """
        return self._query_get_all('VendorCredit', VendorCredits.GET_VENDORS)

    def post(self, data: Dict):
        """
        Post VendorCredits to Quickbooks Online
        :param data: Dict in VendorCredits schema
        :return:
        """
        return self._post_request(data, VendorCredits.POST_VENDOR)
