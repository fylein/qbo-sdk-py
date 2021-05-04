"""
API Base class with util functions
"""
import json
from typing import List, Dict

import requests

from ..exceptions import *


class ApiBase:
    """The base class for all API classes."""

    def __init__(self):
        self.__access_token = None
        self.__server_url = None

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

        response = requests.get(url=request_url.format(start_position), headers=api_headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            query_response = data['QueryResponse']

            while query_response:
                objects.extend(query_response[object_type])
                start_position = start_position + 1000

                data = json.loads(requests.get(url=request_url.format(start_position), headers=api_headers).text)

                query_response = data['QueryResponse']
            return objects

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


    def _query(self, url: str) -> List[Dict]:
        """
        Returns results for query type GET calls
        :param object_type: type of object
        :return: dict of the response
        """
        request_url = '{0}{1}'.format(self.__server_url, url)
        api_headers = {
            'Authorization': 'Bearer {0}'.format(self.__access_token),
            'Accept': 'application/json'
        }

        response = requests.get(url=request_url, headers=api_headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            return data['QueryResponse']

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

        response = requests.get(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result[object_type]

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

        response = requests.post(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            json=data
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result

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

        response = requests.post(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            data=data
        )

        if response.status_code == 200:
            result = json.loads(response.text)
            return result['AttachableResponse'][0]['Attachable']

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
