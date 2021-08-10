"""
Quickbooks Online Tax Codes
"""
from .api_base import ApiBase


class TaxCodes(ApiBase):
    """Class for TaxCode APIs."""

    GET_TAX_CODES = '/query?query=select * from TaxCode STARTPOSITION {0} MAXRESULTS 1000'

    def get(self):
        """Get a list of the existing Tax Code in the Organization.

        Returns:
            Dict in TaxCode schema.
        """
        return self._query_get_all('TaxCode', TaxCodes.GET_TAX_CODES)
