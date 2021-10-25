
import pytest
import logging as logger
from apiautotest.src.Utilities.requestUtilities import RequestUtility
from apiautotest.src.dao.products_dao import Products_DAO
from apiautotest.src.Helpers.ProductHelpers import ProductHelpers

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
@pytest.mark.smoke
def test_get_all_productss():
    req_helper = RequestUtility()
    rs_api = req_helper.get('products')
    assert rs_api, f"Response of list of all products are empty"

@pytest.mark.demo
@pytest.mark.smoke
def test_get_products_by_id():

    # Get a product from DB
    rand_prod= Products_DAO().get_rand_prod_from_db(1)
    rand_prod_id= rand_prod[0]['ID']
    rand_prod_tit= rand_prod[0]['post_title']

    # Make the call
    prod_help =ProductHelpers()
    rs_api= prod_help.get_prod_by_id(rand_prod_id)
    rs_api= rs_api['name']

    # Verify the response
    assert rand_prod_tit==rs_api, f"Get Product by id returned wrong product. ID: {rand_prod_id}" \
                                  f"DB name: {rand_prod_tit}, API name: {rs_api}"
