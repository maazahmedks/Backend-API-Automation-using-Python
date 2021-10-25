
import os

class creds_utility(object):

    def __init__(self):
        pass
    @staticmethod
    def wc_api_keys():
        #        wc_key=os.environ.get('wc_key')
        wc_key="ck_e52a044bb0a207b76b1a76a25f4c3e4976dea27b"
        #        wc_secret=os.environ.get('wc_secret')
        wc_secret="cs_2b8c791882b81d5ee0cc44ca9e9ad8bad44ad042"
        if not wc_key or not wc_secret:
           raise Exception("The environment variables are empty")
        else:
           return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_creds():
        #        db_user=os.environ.get('DB_USER')
        db_user = "root"
        #        db_pass=os.environ.get('DB_PASS')
        db_pass = "root"
        if not db_user or not db_pass:
           raise Exception("The environment variables are empty")
        else:
           return {'db_user': db_user, 'db_pass': db_pass}