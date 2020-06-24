"""
Quickbooks Online preferences
"""
from .api_base import ApiBase


class CompanyInfo(ApiBase):
    """Class for Company Info APIs."""

    GET_COMPANY_INFO = '/companyinfo/{0}'

    def __init__(self, realm_id):
        super().__init__()
        self.__realm_id = realm_id

    def get(self):
        """Get a list of the existing Preferences in the Organization.

        Returns:
            Dict in Preferences schema.
        """
        return self._get_request('CompanyInfo', CompanyInfo.GET_COMPANY_INFO.format(self.__realm_id))
