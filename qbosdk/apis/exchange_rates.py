"""
Quickbooks Online
"""
from datetime import datetime, timedelta
from .api_base import ApiBase


class ExchangeRates(ApiBase):
    """Class for Categories APIs."""

    GET_EXCHANGE_RATES = "/query?query=select * from ExchangeRate where AsOfDate = '{0}' STARTPOSITION " \
                         "{1} MAXRESULTS 1000"
    GET_EXCHANGE_RATES_BY_SOURCE = "/exchangerate?sourcecurrencycode={0}&asofdate={1}"

    def get(self, as_of_date: str = None):
        """
        Get all the exchange rates
        :param as_of_date: date to get rates for (1 day prior if left empty)
        :return: List of Dicts for exchange rates
        """
        if not as_of_date:
            as_of_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        ExchangeRates.GET_EXCHANGE_RATES = ExchangeRates.GET_EXCHANGE_RATES.format(as_of_date, '{0}')
        return self._query_get_all('ExchangeRate', ExchangeRates.GET_EXCHANGE_RATES)

    def get_by_source(self, source_currency_code: str):
        """
        Get all the exchange rates
        :param as_of_date: date to get rates for (1 day prior if left empty)
        :return: List of Dicts for exchange rates
        """
        as_of_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        return self._get_request(
            'ExchangeRate', self.GET_EXCHANGE_RATES_BY_SOURCE.format(source_currency_code, as_of_date))
