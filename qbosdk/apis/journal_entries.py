"""
Quickbooks Online journal entries
"""
from typing import Dict
from .api_base import ApiBase


class JournalEntries(ApiBase):
    """Class for Categories APIs."""

    GET_JOURNAL_ENTRIES = '/query?query=select * from JournalEntry STARTPOSITION {0} MAXRESULTS 1000'
    POST_JOURNAL_ENTRY = '/journalentry?minorversion=38'

    def get(self):
        """
        Get all JournalEntries
        :return: List of Dicts in JournalEntry Schema
        """
        return self._query_get_all('JournalEntry', JournalEntries.GET_JOURNAL_ENTRIES)

    def post(self, data: Dict):
        """
        Post JournalEntry (check, etc) to Quickbooks Online
        :param data: Dict in JournalEntry schema
        :return:
        """
        return self._post_request(data, JournalEntries.POST_JOURNAL_ENTRY)
