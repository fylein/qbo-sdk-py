"""
Quickbooks Online TaxRates
"""
from .api_base import ApiBase


class TaxRates(ApiBase):
    """Class for TaxRates APIs."""

    GET_TAX_RATES = '/query?query=select * from TaxRate STARTPOSITION {0} MAXRESULTS 1000'
    GET_TAX_RATES_BY_ID = '/taxrate/{0}'

    def get(self):
        """
        Get all Taxrates
        :return: List of Dicts in Taxrates Schema
        """
        return self._query_get_all('TaxRate', TaxRates.GET_TAX_RATES)

    def get_by_id(self, taxrateId: str):
        """
        Get Taxrates from Quickbooks Online
        :param taxrateId: Taxrate Id
        :return: Dict Response
        """
        return self._get_request('TaxRate', TaxRates.GET_TAX_RATES_BY_ID.format(taxrateId))
