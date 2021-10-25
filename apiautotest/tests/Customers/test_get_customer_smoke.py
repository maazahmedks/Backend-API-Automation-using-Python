
import pytest
import logging as logger
from apiautotest.src.Utilities.requestUtilities import RequestUtility


@pytest.mark.customer
@pytest.mark.smoke
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtility()
    rs_api = req_helper.get('customers')
    assert rs_api, f"Response of list of all customers is empty"