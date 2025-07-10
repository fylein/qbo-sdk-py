"""
API Base class with util functions
"""
import logging
import json
from typing import List, Dict, Generator

import requests

from ..exceptions import WrongParamsError, InvalidTokenError, QuickbooksOnlineSDKError, \
    NoPrivilegeError, NotFoundItemError, ExpiredTokenError, InternalServerError

logger = logging.getLogger(__name__)

class ApiBase:
    """The base class for all API classes."""

    def __init__(self):
        self.__access_token = None
        self.__server_url = None
        self.__minor_version = None

    def change_access_token(self, access_token):
        """
        Sets the access token for APIs
        :param access_token: acceess token (JWT)
        :return: None
        """
        self.__access_token = access_token

    def set_server_url(self, server_url: str):
        """
        Set the server url for APIs
        :param server_url: Url with realm id
        :return: None
        """
        self.__server_url = server_url

    def set_minor_version(self, minor_version: str):
        """
        Set the minor version to be appended to every request.
        :param minor_version: minor version string or int
        """
        self.__minor_version = str(minor_version) if minor_version is not None else None

    def _append_minor_version(self, url: str) -> str:
        """
        If a minor version is set, append ?minorversion=<mv> or &minorversion=<mv> to `url`.
        """
        if not self.__minor_version:
            return url
        sep = "&" if "?" in url else "?"
        return f"{url}{sep}minorversion={self.__minor_version}"

    def _query_get_all(self, object_type: str, url: str) -> List[Dict]:
        """
        Gets all the objects of a particular type for query type GET calls
        :param url: GET URL of object
        :param object_type: type of object
        :return: list of objects
        """
        start_position = 1

        request_url = '{0}{1}'.format(self.__server_url, url)

        objects = []

        api_headers = {
            'Authorization': 'Bearer {0}'.format(self.__access_token),
            'Accept': 'application/json'
        }

        response = requests.get(
            url=self._append_minor_version(request_url.format(start_position)),
            headers=api_headers
        )

        if response.status_code == 200:
            logger.debug('Response for get request for url: %s, %s', url, response.text)
            data = json.loads(response.text)
            query_response = data['QueryResponse']

            while query_response:
                objects.extend(query_response[object_type])
                start_position = start_position + 1000

                data = json.loads(
                    requests.get(
                        url=self._append_minor_version(request_url.format(start_position)),
                        headers=api_headers
                    ).text
                )

                query_response = data['QueryResponse']
            return objects

        logger.info('Response for get request for url: %s, %s', url, response.text)
        if response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        if response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        if response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        if response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        if response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        if response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        raise QuickbooksOnlineSDKError('Error: {0}'.format(response.status_code), response.text)

    def _query_get_all_generator(self, object_type: str, url: str) -> Generator[Dict, None, None]:
        """
        Gets all the objects of a particular type for query type GET calls
        :param url: GET URL of object
        :param object_type: type of object
        :return: list of objects
        """
        start_position = 1
        max_results = 1000

        request_url = '{0}{1}'.format(self.__server_url, url)

        api_headers = {
            'Authorization': 'Bearer {0}'.format(self.__access_token),
            'Accept': 'application/json'
        }

        while True:
            try:
                response = requests.get(
                    url=self._append_minor_version(request_url.format(start_position)),
                    headers=api_headers
                )
                response.raise_for_status()

                data = json.loads(response.text)
                query_response = data['QueryResponse']

                if not query_response or object_type not in query_response:
                    break

                logger.debug('Response for get request for url: %s, %s', url, response.text)

                yield query_response[object_type]

                # If we got fewer results than max_results, we've reached the end
                if len(query_response[object_type]) < max_results:
                    break

                start_position += max_results

            except requests.exceptions.HTTPError as err:
                logger.info('Response for get request for url: %s, %s', url, err.response.text)
                if err.response.status_code == 400:
                    raise WrongParamsError('Some of the parameters are wrong', err.response.text) from err

                if err.response.status_code == 401:
                    raise InvalidTokenError('Invalid token, try to refresh it', err.response.text) from err

                if err.response.status_code == 403:
                    raise NoPrivilegeError('Forbidden, the user has insufficient privilege', err.response.text) from err

                if err.response.status_code == 404:
                    raise NotFoundItemError('Not found item with ID', err.response.text) from err

                if err.response.status_code == 498:
                    raise ExpiredTokenError('Expired token, try to refresh it', err.response.text) from err

                if err.response.status_code == 500:
                    raise InternalServerError('Internal server error', err.response.text) from err

                raise QuickbooksOnlineSDKError('Error: {0}'.format(err.response.status_code),
                                               err.response.text) from err

    def _query(self, url: str) -> List[Dict]:
        """
        Returns results for query type GET calls
        :param object_type: type of object
        :return: dict of the response
        """
        request_url = '{0}{1}'.format(self.__server_url, url)
        request_url = self._append_minor_version(request_url)

        api_headers = {
            'Authorization': 'Bearer {0}'.format(self.__access_token),
            'Accept': 'application/json'
        }

        response = requests.get(url=request_url, headers=api_headers)

        if response.status_code == 200:
            logger.debug('Response for get request for url: %s, %s', url, response.text)
            data = json.loads(response.text)
            return data['QueryResponse'] if 'QueryResponse' in data else data

        logger.info('Response for get request for url: %s, %s', url, response.text)
        if response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        if response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        if response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        if response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        if response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        if response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        raise QuickbooksOnlineSDKError('Error: {0}'.format(response.status_code), response.text)

    def _get_request(self, object_type: str, api_url: str) -> List[Dict] or Dict:
        """Create a HTTP GET request.

        Parameters:
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {
            'Authorization': 'Bearer {0}'.format(self.__access_token),
            'Accept': 'application/json'
        }

        api_url = self._append_minor_version(api_url)

        response = requests.get(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers
        )

        if response.status_code == 200:
            logger.debug('Response for get request for url: %s, %s', api_url, response.text)
            result = json.loads(response.text)
            return result[object_type]

        logger.info('Response for get request for url: %s, %s', api_url, response.text)
        if response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        if response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        if response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        if response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        if response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        if response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        raise QuickbooksOnlineSDKError('Error: {0}'.format(response.status_code), response.text)

    def _post_request(self, data, api_url):
        """Create a HTTP post request.

        Parameters:
            data (dict): HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.__access_token)
        }

        api_url = self._append_minor_version(api_url)

        response = requests.post(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            json=data
        )

        if response.status_code == 200:
            logger.debug('Response for post request: %s', response.text)
            result = json.loads(response.text)
            return result

        logger.debug('Payload for post request: %s', data)
        logger.info('Response for post request: %s', response.text)

        if response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        if response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        if response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        if response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        if response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        if response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        raise QuickbooksOnlineSDKError('Error: {0}'.format(response.status_code), response.text)

    def _post_file(self, data, api_url):
        """Create a HTTP post request.

        Parameters:
            data (str): HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {
            'Content-Type': 'multipart/form-data; boundary={0}'.format('YOjcLaTlykb6OxfYJx4O07j1MweeMFem'),
            'Accept': 'application/json',
            'Connection': 'close',
            'Authorization': 'Bearer {0}'.format(self.__access_token)
        }

        api_url = self._append_minor_version(api_url)

        response = requests.post(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            data=data
        )

        if response.status_code == 200:
            logger.debug('Response for post request: %s', response.text)
            result = json.loads(response.text)
            return result['AttachableResponse'][0]['Attachable']


        logger.debug('Payload for post request: %s', data)
        logger.info('Response for post request: %s', response.text)

        if response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        if response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        if response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        if response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        if response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        if response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        raise QuickbooksOnlineSDKError('Error: {0}'.format(response.status_code), response.text)
