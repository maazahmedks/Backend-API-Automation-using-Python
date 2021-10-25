
from apiautotest.src.Utilities.GenericUtilities import generate_rand_email_and_pass
from apiautotest.src.Utilities.requestUtilities import RequestUtility
from apiautotest.src.Utilities.requestUtilities import RequestUtility
import logging as logger

class ProductHelpers(object):

      def __init__(self):
        self.request_utility= RequestUtility()

      def get_prod_by_id(self, prod_id):
        return self.request_utility.get(f"products/{prod_id}")

      def call_create_payload(self, payload):
        test = self.request_utility.apost('products', payload=payload, expected_status_code=201)
        return test

      def call_list_products(self, payload=None):
         max_pages=1000
         all_products = []
         for i in range(1, max_pages + 1):
             logger.debug(f"List producsts page number: {i}")

             if not 'per_page' in payload.keys():
                 payload['per_page']=100

            # add the currnet page number to the call
             payload['page'] = i
             test2 = self.request_utility.get('products', payload=payload)

            # If there is no response then stop the loop b/c there are no more products
             if not test2:
              "break"
             else:
               all_products.extend(test2)
         else:
            raise Exception(f"Unable to find all products after {max_pages} pages")

         return test2