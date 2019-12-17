class QuickbookOnlineSDKError(Exception):
    """The base exception class for QBOSDK.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(QuickbookOnlineSDKError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        return repr(self.message)


class NotFoundClientError(QuickbookOnlineSDKError):
    """Client not found OAuth2 authorization, 404 error."""
    pass


class UnauthorizedClientError(QuickbookOnlineSDKError):
    """Wrong client secret and/or refresh token, 401 error."""
    pass


class ExpiredTokenError(QuickbookOnlineSDKError):
    """Expired (old) access token, 498 error."""
    pass


class InvalidTokenError(QuickbookOnlineSDKError):
    """Wrong/non-existing access token, 401 error."""
    pass


class NoPrivilegeError(QuickbookOnlineSDKError):
    """The user has insufficient privilege, 403 error."""
    pass


class WrongParamsError(QuickbookOnlineSDKError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""
    pass


class NotFoundItemError(QuickbookOnlineSDKError):
    """Not found the item from URL, 404 error."""
    pass


class InternalServerError(QuickbookOnlineSDKError):
    """The rest QBOSDK errors, 500 error."""
    pass
