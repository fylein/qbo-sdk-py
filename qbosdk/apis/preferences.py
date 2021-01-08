"""
Quickbooks Online preferences
"""
from .api_base import ApiBase


class Preferences(ApiBase):
    """Class for Categories APIs."""

    GET_PREFERENCES = '/preferences'

    def get(self):
        """Get a list of the existing Preferences in the Organization.

        Returns:
            Dict in Preferences schema.
        """
        return self._get_request(Preferences.GET_PREFERENCES)
