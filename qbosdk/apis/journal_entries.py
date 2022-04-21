"""
Quickbooks Online journal entries
"""
from typing import Dict
from .api_base import ApiBase


class JournalEntries(ApiBase):
    """Class for Categories APIs."""

    GET_JOURNAL_ENTRIES = '/query?query=select * from JournalEntry STARTPOSITION {0} MAXRESULTS 1000'
    POST_JOURNAL_ENTRY = '/journalentry?minorversion=53'
    DELETE_JOURNAL_ENTRY = '/journalentry?operation=delete'

    def get(self):
        """
        Get all JournalEntries
        :return: List of Dicts in JournalEntry Schema
        """
        return self._query_get_all('JournalEntry', JournalEntries.GET_JOURNAL_ENTRIES)

    def post(self, data: Dict):
        """
        Post JournalEntry to Quickbooks Online
        :param data: Dict in JournalEntry schema
        :return:
        """
        return self._post_request(data, JournalEntries.POST_JOURNAL_ENTRY)

    def delete(self, journal_entry_id: str):
        """
        Delete JournalEntry from Quickbooks Online
        :param journal_entry_id: Journal Entry Id to remove
        :return: Dict response
        """
        data = {
            'Id': journal_entry_id,
            'SyncToken': '1'
        }
        return self._post_request(data, JournalEntries.DELETE_JOURNAL_ENTRY)
