"""
Quickbooks Online Tax Codes
"""
from .api_base import ApiBase


class TaxCodes(ApiBase):
    """Class for TaxCode APIs."""

    GET_TAX_CODES = '/query?query=select * from TaxCode'
    COUNT_TAX_CODES = '/query?query=select count(*) from TaxCode where Active = True'

    def get(self):
        """Get a list of the existing Tax Code in the Organization.

        Returns:
            Dict in TaxCode schema.
        """
        query = TaxCodes.GET_TAX_CODES + " STARTPOSITION {0} MAXRESULTS 1000"
        return self._query_get_all('TaxCode', query)

    def get_all_generator(self, last_updated_time = None):
        """Get a list of the existing Tax Code in the Organization.

        Returns:
            Generator with dicts in TaxCode schema.
        """
        query = TaxCodes.GET_TAX_CODES
        if last_updated_time:
            query += f" where Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"

        return self._query_get_all_generator('TaxCode', query)

    def get_inactive(self, last_updated_time: None):

        """
        Retrieves a list of inactive tax codes from the QuickBooks Online API.

        :param last_updated_time: The last updated time to filter the tax codes.
        :return: A list of inactive tax codes.
        """
        query = TaxCodes.GET_TAX_CODES + " where Active=false"
        if last_updated_time:
            query += f" and Metadata.LastUpdatedTime >= '{last_updated_time}'"
        query += " STARTPOSITION {0} MAXRESULTS 1000"
        return self._query_get_all_generator('TaxCode', query)

    def count(self):
        """Get count of Tax codes in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(TaxCodes.COUNT_TAX_CODES)['totalCount']
