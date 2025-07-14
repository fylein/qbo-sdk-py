"""
Quickbooks Online vendors
"""
from typing import Dict

from .api_base import ApiBase


class Vendors(ApiBase):
    """Class for Categories APIs."""

    GET_VENDORS = '/query?query=select * from Vendor STARTPOSITION {0} MAXRESULTS 1000'
    POST_VENDOR = '/vendor'
    SEARCH_VENDOR = "/query?query=select * from Vendor where DisplayName = '{0}'"
    COUNT_VENDORS = '/query?query=select count(*) from Vendor where Active = True'

    def get(self):
        """Get a list of the existing Vendors in the Organization.

        Returns:
            List with dicts in Vendors schema.
        """
        return self._query_get_all('Vendor', Vendors.GET_VENDORS)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing Vendors in the Organization.

        Returns:
            Generator with dicts in Vendors schema.
        """
        if last_updated_time:
            Vendors.GET_VENDORS = Vendors.GET_VENDORS.replace(
                'from Vendor',
                f"from Vendor where MetaData.LastUpdatedTime > '{last_updated_time}'"
            )

        return self._query_get_all_generator('Vendor', Vendors.GET_VENDORS)

    def post(self, data: Dict):
        """
        Post Vendor to Quickbooks Online
        :param data: Dict in Vendor schema
        :return:
        """
        return self._post_request(data, Vendors.POST_VENDOR)

    def search_vendor_by_display_name(self, display_name=None):
        """
        Search vendor by display name
        :param display_name: Quickbooks Vendor Display Name
        :return: Vendor
        """
        response = self._get_request('QueryResponse', Vendors.SEARCH_VENDOR.format(display_name))

        return response['Vendor'][0] if 'Vendor' in response else None

    def get_inactive(self, last_updated_time: None):
        """
        Retrieves a list of inactive vendors from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the vendors.
        :return: A list of inactive vendors.
        """

        QUERY = "/query?query=select * from Vendor where Active=false"
        if last_updated_time:
            QUERY += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        QUERY += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('Vendor', QUERY)

    def count(self):
        """Get count of Vendors in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(Vendors.COUNT_VENDORS)['totalCount']
