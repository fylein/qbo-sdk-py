"""
Quickbooks Online journal entries
"""
from typing import Dict
from .api_base import ApiBase


class JournalEntries(ApiBase):
    """Class for Categories APIs."""

    GET_JOURNAL_ENTRIES = '/query?query=select * from JournalEntry STARTPOSITION {0} MAXRESULTS 1000'
    POST_JOURNAL_ENTRY = '/journalentry'
    DELETE_JOURNAL_ENTRY = '/journalentry?operation=delete'
    GET_JOURNAL_ENTRY_BY_ID = '/journalentry/{0}'

    def get(self):
        """
        Get all JournalEntries
        :return: List of Dicts in JournalEntry Schema
        """
        return self._query_get_all('JournalEntry', JournalEntries.GET_JOURNAL_ENTRIES)

    def get_all_generator(self):
        """
        Get all JournalEntries
        :return: Generator with Dicts in JournalEntry Schema
        """
        return self._query_get_all_generator('JournalEntry', JournalEntries.GET_JOURNAL_ENTRIES)

    def post(self, data: Dict):
        """
        Post JournalEntry to Quickbooks Online
        :param data: Dict in JournalEntry schema
        :return:
        """
        return self._post_request(data, JournalEntries.POST_JOURNAL_ENTRY)

    def get_by_id(self, journal_entry_id):
        """
        Get JournalEntry by Id
        :param journal_entry_id: Journal Entry Id
        :return: Dict in JournalEntry schema
        """
        return self._get_request('JournalEntry', JournalEntries.GET_JOURNAL_ENTRY_BY_ID.format(journal_entry_id))

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
