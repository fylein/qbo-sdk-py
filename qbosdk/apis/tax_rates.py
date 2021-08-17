"""
Quickbooks Online Tax Codes
"""
from .api_base import ApiBase


class TaxRates(ApiBase):
    """Class for TaxRates APIs."""

    GET_TAX_RATES = '/query?query=select * from TaxRate STARTPOSITION {0} MAXRESULTS 1000'
    GET_TAX_RATES_BY_ID = '/taxrate/{0}'

    def get(self):
        """
        Get all Bills
        :return: List of Dicts in Bill Schema
        """
        return self._query_get_all('TaxRate', TaxRates.GET_TAX_RATES)

    def get_by_id(self, taxrateId):
        """
        Get Bill from Quickbooks Online
        :param bill_id: Bill Id
        :return: Dict Response
        """
        return self._get_request('TaxRate', TaxRates.GET_TAX_RATES_BY_ID.format(taxrateId))