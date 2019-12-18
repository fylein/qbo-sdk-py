"""
Quickbooks Online attachables
"""
import json
import textwrap
from typing import Dict

from .api_base import ApiBase


class Attachments(ApiBase):
    """Class for Categories APIs."""

    GET_ATTACHABLES = '/query?query=select * from Attachable STARTPOSITION {0} MAXRESULTS 1000'
    POST_ATTACHABLE = '/attachable'
    POST_FILE = '/upload'

    def get(self):
        """
        Get all Attachables
        :return: List of Dicts in Attachable Schema
        """
        return self._query_get_all('Attachable', Attachments.GET_ATTACHABLES)

    def post(self, ref_id: str, ref_type: str, content, file_name):
        """
        Post Attachable (check, etc) to Quickbooks Online
        :param file_name: name of the file
        :param content: attachment content
        :param ref_type: type of object
        :param ref_id: object id
        :return: Dict in attachable schema
        """
        file = self.__upload_file(content, file_name)
        if file:
            attachable_ref = [
                {
                    'EntityRef': {
                        'type': ref_type,
                        'value': ref_id
                    }
                }
            ]
            file['AttachableRef'] = attachable_ref
        return self._post_request(file, Attachments.POST_ATTACHABLE)

    def __upload_file(self, content, file_name: str) -> Dict:
        """
        Upload file to Quickbooks
        :param content: Content in base64
        :param file_name: name of the file
        :return: Returns file object as Dict
        """
        binary_data = content

        boundary = 'YOjcLaTlykb6OxfYJx4O07j1MweeMFem'

        content_type = self.__get_content_type(file_name)

        body = {
            'Content-Type': content_type
        }

        if content_type:
            request_body = textwrap.dedent(
                """
                --%s
                Content-Disposition: form-data; name="file_metadata_01";
                Content-Type: application/json
                %s
                --%s
                Content-Disposition: form-data; name="file_content_01"; filename="%s"
                Content-Type: %s
                Content-Transfer-Encoding: base64

                %s

                --%s--
                """
            ) % (boundary, json.dumps(body), boundary, file_name, content_type, binary_data, boundary)

            return self._post_file(str(request_body), Attachments.POST_FILE)

        return {}

    @staticmethod
    def __get_content_type(file_name: str) -> str or None:
        """
        Gets content type of supported file types
        :param file_name: name of the file
        :return: content-type or None
        """
        extension = file_name.split('.')[-1]

        content_types: Dict = {
            'ai': 'application/postscript',
            'csv': 'text/csv',
            'doc': 'application/msword',
            'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'eps': 'application/postscript',
            'gif': 'image/gif',
            'jpeg': 'image/jpeg',
            'jpg': 'image/jpg',
            'png': 'image/png',
            'ods': 'application/vnd.oasis.opendocument.spreadsheet',
            'pdf': 'application/pdf',
            'rtf': 'text/rtf',
            'tif': 'image/tiff',
            'txt': 'text/plain',
            'xls': 'application/vnd.ms-excel',
            'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'xml': 'text/xml'
        }

        return content_types.get(extension.lower())
