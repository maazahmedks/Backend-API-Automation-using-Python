
import pytest
from apiautotest.src.Utilities.GenericUtilities import generate_rand_string
from apiautotest.src.Helpers.ProductHelpers import ProductHelpers
from apiautotest.src.dao.products_dao import Products_DAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.smoke
@pytest.mark.tcid26
def test_create_all_product():

    # Generate some data
      payload= dict()
      payload['name']= generate_rand_string(20)
      payload['type'] = 'simple'
      payload['regular_price'] = '25.67'

    # Make API call
      ph=ProductHelpers()
      product_c = ph.call_create_payload(payload)
      import pdb; pdb.set_trace()

    # Verify the response is not empty
      assert product_c, f"Create product API response is empty. Payload: {payload}"
      assert product_c['name'] == payload['name'], f"Create product API reply unexpected name" \
        f"Unexpected Name. Expected: {payload['name']}, Actual: {product_c['name']}"

    # Verfiy that product exist in DB
      prod_id = product_c['id']
      pddao=Products_DAO()
      db_prod = pddao.get_prod_by_id(prod_id)
      import pdb; pdb.set_trace()
      assert payload['name'] == db_prod[0]['post_title'], f"Create product, title in db does not match"

#      import pdb; pdb.set_trace()