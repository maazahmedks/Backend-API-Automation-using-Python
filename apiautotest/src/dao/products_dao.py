
import random
from apiautotest.src.Utilities.DbUtility import DBUtility

class Products_DAO:

    def __init__(self):
        self.db_helper=DBUtility()

    def get_rand_prod_from_db(self, qty=1):

        sql='SELECT * FROM local.wp_posts WHERE post_type="product" LIMIT 5000;'
        rs_sql=self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))


    def get_prod_by_id(self, prod_id):
        sql=f'SELECT * FROM local.wp_posts where ID={prod_id};'
        return self.db_helper.execute_select(sql)

    def get_prod_created_after_given_date(self, _date):
        sql=f'SELECT * FROM local.wp_posts where post_type="product" and post_date > "{_date}" limit 10000'
        return self.db_helper.execute_select(sql)