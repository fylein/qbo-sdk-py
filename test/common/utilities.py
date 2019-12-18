import json
import logging
from os import path
from unittest.mock import Mock

from qbosdk import QuickbooksOnlineSDK
logger = logging.getLogger(__name__)


def get_mock_qbo_dict(filename):
    basepath = path.dirname(__file__)
    filepath = path.join(basepath, filename)
    mock_qbo_json = open(filepath, 'r').read()
    mock_qbo_dict = json.loads(mock_qbo_json)
    return mock_qbo_dict


def get_mock_qbo_from_file(filename):
    mock_qbo_dict = get_mock_qbo_dict(filename)
    mock_qbo = Mock()
    mock_qbo.accounts.get.return_value = mock_qbo_dict['accounts']
    mock_qbo.employees.get.return_value = mock_qbo_dict['employees']
    mock_qbo.departments.get.return_value = mock_qbo_dict['departments']
    mock_qbo.classes.get.return_value = mock_qbo_dict['classes']
    mock_qbo.exchange_rates.get.return_value = mock_qbo_dict['exchange_rates']
    mock_qbo.preferences.get.return_value = mock_qbo_dict['preferences']
    mock_qbo.journal_entries.get.return_value = mock_qbo_dict['journal_entries']
    mock_qbo.purchases.get.return_value = mock_qbo_dict['purchases']
    mock_qbo.attachments.get.return_value = mock_qbo_dict['attachments']
    return mock_qbo


def get_mock_qbo():
    return get_mock_qbo_from_file('mock_qbo.json')


def dict_compare_keys(d1, d2, key_path=''):
    """
    Compare two dicts recursively and see if dict1 has any keys that dict2 does not
    Returns: list of key paths
    """
    res = []
    if not d1:
        return res
    if not isinstance(d1, dict):
        return res
    for k in d1:
        if k not in d2:
            missing_key_path = f'{key_path}->{k}'
            res.append(missing_key_path)
        else:
            if isinstance(d1[k], dict):
                key_path1 = f'{key_path}->{k}'
                res1 = dict_compare_keys(d1[k], d2[k], key_path1)
                res = res + res1
            elif isinstance(d1[k], list):
                key_path1 = f'{key_path}->{k}[0]'
                dv1 = d1[k][0] if len(d1[k]) > 0 else None
                dv2 = d2[k][0] if len(d2[k]) > 0 else None
                res1 = dict_compare_keys(dv1, dv2, key_path1)
                res = res + res1
    return res


def qbo_connect():
    """
    QBO Connector connection
    :param: db connection
    """
    file = open('test_credentials.json', 'r')
    quickbooks_config = json.load(file)

    connection = QuickbooksOnlineSDK(
        client_id=quickbooks_config['client_id'],
        client_secret=quickbooks_config['client_secret'],
        refresh_token=quickbooks_config['refresh_token'],
        realm_id=quickbooks_config['realm_id'],
        environment=quickbooks_config['environment']
    )

    quickbooks_config['refresh_token'] = connection.refresh_token

    with open('test_credentials.json', 'w') as fp:
        json.dump(quickbooks_config, fp)
    return connection
