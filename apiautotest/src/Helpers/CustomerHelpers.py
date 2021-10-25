
from apiautotest.src.Utilities.GenericUtilities import generate_rand_email_and_pass
from apiautotest.src.Utilities.requestUtilities import RequestUtility

class CustomerHelpers(object):


    def create_customers(self, email=None, password=None, **kwargs):
        if not email:
            data=generate_rand_email_and_pass()
            email=data['email']
        if not password:
            password='password123'

        payload= dict()
        payload['email']=email
#        payload['password']=password
        payload.update(kwargs)
        obj=RequestUtility()
        Create_user_json = obj.apost(endpoint='customers', payload=payload, expected_status_code=201)

        return Create_user_json