"""
Quickbooks Online Tax Codes
"""
from .api_base import ApiBase


class TaxCodes(ApiBase):
    """Class for TaxCode APIs."""

    GET_TAX_CODES = '/query?query=select * from TaxCode STARTPOSITION {0} MAXRESULTS 1000'
    COUNT_TAX_CODES = '/query?query=select count(*) from TaxCode where Active = True'

    def get(self):
        """Get a list of the existing Tax Code in the Organization.

        Returns:
            Dict in TaxCode schema.
        """
        return self._query_get_all('TaxCode', TaxCodes.GET_TAX_CODES)

    def get_all_generator(self):
        """Get a list of the existing Tax Code in the Organization.

        Returns:
            Generator with dicts in TaxCode schema.
        """
        return self._query_get_all_generator('TaxCode', TaxCodes.GET_TAX_CODES)

    def count(self):
        """Get count of Tax codes in the Organization.

        Returns:
            Count in Int.
        """
        return self._query(TaxCodes.COUNT_TAX_CODES)['totalCount']
