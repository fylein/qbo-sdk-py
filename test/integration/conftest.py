import logging
import pytest

from test.common.utilities import get_mock_qbo, qbo_connect

logger = logging.getLogger(__name__)


@pytest.fixture
def mock_qbo():
    return get_mock_qbo()


@pytest.fixture(scope='module')
def qbo():
    return qbo_connect()


