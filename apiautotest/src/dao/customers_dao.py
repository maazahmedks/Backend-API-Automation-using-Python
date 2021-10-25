
import random
from apiautotest.src.Utilities.DbUtility import DBUtility

class Customer_DAO:

    def __init__(self):
        self.db_helper=DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        sql = "SELECT * FROM local.wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))

