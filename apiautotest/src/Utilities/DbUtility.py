import pymysql
import logging as logger
from apiautotest.src.Utilities.CredentialsUtility import creds_utility

class DBUtility(object):

    def __init__(self):
        creds_helper= creds_utility()
        self.creds= creds_helper.get_db_creds()
        self.host='localhost'
        pass

    def create_connection(self, sql):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'], password=self.creds['db_pass'], port=10005, )
        return connection

    def execute_select(self, sql):
        connect = self.create_connection(sql)

        try:
            logger.debug(f"Executing: {sql}")
            con=connect.cursor(pymysql.cursors.DictCursor)
            con.execute(sql)
            rs_dict= con.fetchall()
            con.close()
        except Exception as e:
            raise Exception(f"Failed to execute SQL: {sql} \n . Error: {str(e)} ")
        finally:
            con.close()

        return rs_dict

    def execute_crud(self, sql):
        pass