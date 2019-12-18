import logging
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)


def test_accounts(qbo, mock_qbo):
    """
    Test Quickbooks accounts Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    accounts = qbo.accounts.get()
    mock_accounts = mock_qbo.accounts.get()

    assert dict_compare_keys(accounts[0], mock_accounts[0]) == [], 'qbo.accounts.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_accounts[0], accounts[0]) == [], 'mock_qbo.accounts.get() has stuff that qbo doesnt'


def test_departments(qbo, mock_qbo):
    """
    Test Quickbooks departments Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    departments = qbo.departments.get()
    mock_departments = mock_qbo.departments.get()

    assert dict_compare_keys(departments[0], mock_departments[0]) == [], \
        'qbo.departments.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_departments[0], departments[0]) == [], \
        'mock_qbo.departments.get() has stuff that qbo doesnt'
    

def test_employees(qbo, mock_qbo):
    """
    Test Quickbooks employees Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    employees = qbo.employees.get()
    mock_employees = mock_qbo.employees.get()

    assert dict_compare_keys(employees[0], mock_employees[0]) == [], \
        'qbo.employees.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_employees[0], employees[0]) == [], \
        'mock_qbo.employees.get() has stuff that qbo doesnt'


def test_classes(qbo, mock_qbo):
    """
    Test Quickbooks classes Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    classes = qbo.classes.get()
    mock_classes = mock_qbo.classes.get()

    assert dict_compare_keys(classes[0], mock_classes[0]) == [], \
        'qbo.classes.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_classes[0], classes[0]) == [], \
        'mock_qbo.classes.get() has stuff that qbo doesnt'


def test_exchange_rates(qbo, mock_qbo):
    """
    Test Quickbooks exchange_rates Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    exchange_rates = qbo.exchange_rates.get()
    mock_exchange_rates = mock_qbo.exchange_rates.get()

    assert dict_compare_keys(exchange_rates[0], mock_exchange_rates[0]) == [], \
        'qbo.exchange_rates.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_exchange_rates[0], exchange_rates[0]) == [], \
        'mock_qbo.exchange_rates.get() has stuff that qbo doesnt'


def test_preferences(qbo, mock_qbo):
    """
    Test Quickbooks preferences Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    preferences = qbo.preferences.get()
    mock_preferences = mock_qbo.preferences.get()

    assert dict_compare_keys(preferences, mock_preferences) == [], \
        'qbo.preferences.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_preferences, preferences) == [], \
        'mock_qbo.preferences.get() has stuff that qbo doesnt'


def test_journal_entries(qbo, mock_qbo):
    """
    Test Quickbooks journal_entries Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    journal_entries = qbo.journal_entries.get()
    mock_journal_entries = mock_qbo.journal_entries.get()

    assert dict_compare_keys(journal_entries[0], mock_journal_entries[0]) == [], \
        'qbo.journal_entries.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_journal_entries[0], journal_entries[0]) == [], \
        'mock_qbo.journal_entries.get() has stuff that qbo doesnt'


def test_purchases(qbo, mock_qbo):
    """
    Test Quickbooks purchases Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    purchases = qbo.purchases.get()
    mock_purchases = mock_qbo.purchases.get()

    assert dict_compare_keys(purchases[0], mock_purchases[0]) == [], \
        'qbo.purchases.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_purchases[0], purchases[0]) == [], \
        'mock_qbo.purchases.get() has stuff that qbo doesnt'


def test_attachments(qbo, mock_qbo):
    """
    Test Quickbooks attachments Object
    :param qbo: qbo sdk instance
    :param mock_qbo: mock instance
    :return: None
    """
    attachments = qbo.attachments.get()
    mock_attachments = mock_qbo.attachments.get()

    assert dict_compare_keys(attachments[0], mock_attachments[0]) == [], \
        'qbo.attachments.get() has stuff that mock_qbo doesnt'
    assert dict_compare_keys(mock_attachments[0], attachments[0]) == [], \
        'mock_qbo.attachments.get() has stuff that qbo doesnt'
