"""
Quickbooks Online SDK Exceptions
"""


class QuickbooksOnlineSDKError(Exception):
    """The base exception class for QBOSDK.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(QuickbooksOnlineSDKError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        return repr(self.message)


class NotFoundClientError(QuickbooksOnlineSDKError):
    """Client not found OAuth2 authorization, 404 error."""


class UnauthorizedClientError(QuickbooksOnlineSDKError):
    """Wrong client secret and/or refresh token, 401 error."""


class ExpiredTokenError(QuickbooksOnlineSDKError):
    """Expired (old) access token, 498 error."""


class InvalidTokenError(QuickbooksOnlineSDKError):
    """Wrong/non-existing access token, 401 error."""


class NoPrivilegeError(QuickbooksOnlineSDKError):
    """The user has insufficient privilege, 403 error."""


class WrongParamsError(QuickbooksOnlineSDKError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""


class NotFoundItemError(QuickbooksOnlineSDKError):
    """Not found the item from URL, 404 error."""


class InternalServerError(QuickbooksOnlineSDKError):
    """The rest QBOSDK errors, 500 error."""
