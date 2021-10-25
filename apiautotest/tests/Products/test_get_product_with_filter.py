
import pytest
from datetime import datetime, timedelta
from apiautotest.src.Helpers.ProductHelpers import ProductHelpers
from apiautotest.src.dao.products_dao import Products_DAO
import pdb

@pytest.mark.regression
class TestListProdWithFilter(object):

    @pytest.mark.tcid51
    @pytest.mark.smoke
    def test_list_prod_with_filter(self):

        # Create data
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

#        _after_created_date = datetime.now() - timedelta(days=x_days_from_today)
#        after_created_date = _after_created_date.strftime('%Y-%M-%dT%H:%m:%S')

        payload = dict()
        payload['after'] = after_created_date
        payload['per_page'] = 100

        # Make the call
        _rs_api = ProductHelpers()
        rs_api = _rs_api.call_list_products(payload)
        assert rs_api, f"Empty response of list of products by filters"
        pdb.set_trace()

        # Get data from db
        Prod_dao = Products_DAO()
        Prod_dao2 = Prod_dao.get_prod_created_after_given_date(after_created_date)
        pdb.set_trace()


        # Verify response
        assert len(rs_api) == len(Prod_dao2), f"List products with filter after is not same"

        id_rs_api = [i['id'] for i in rs_api]
        id_db = [i['ID'] for i in Prod_dao2]

        id_diff = list(set(id_rs_api) - set(id_db))
        assert not id_diff, f"List producsts with filters. Product ID in DB mismatch"
