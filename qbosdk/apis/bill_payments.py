"""
Quickbooks Online Bill Payments
"""
from typing import Dict
from .api_base import ApiBase


class BillPayments(ApiBase):
    """Class for Bill Payments API."""

    GET_BILLS = '/query?query=select * from billpayment STARTPOSITION {0} MAXRESULTS 1000'
    POST_BILL_PAYMENT = '/billpayment?minorversion=38'
    DELETE_BILL = '/billpayment?operation=delete'

    def get(self):
        """
        Get all Bill Payments
        :return: List of Dicts in Bill Payment Schema
        """
        return self._query_get_all('BillPayment', BillPayments.GET_BILLS)

    def post(self, data: Dict):
        """
        Post Bill Payment to Quickbooks Online
        :param data: Dict in Bill Payment schema
        :return:
        """
        return self._post_request(data, BillPayments.POST_BILL_PAYMENT)

    def delete(self, bill_payment_id: str):
        """
        Delete Bill Payment from Quickbooks Online
        :param bill_payment_id: Bill Payment Id to remove
        :return: Dict response
        """
        data = {
            'SyncToken': '1',
            'Id': bill_payment_id
        }
        return self._post_request(data, BillPayments.DELETE_BILL)
