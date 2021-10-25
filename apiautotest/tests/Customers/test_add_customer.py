
import pytest
import logging as logger
from apiautotest.src.Utilities.GenericUtilities import generate_rand_email_and_pass
from apiautotest.src.Helpers.CustomerHelpers import CustomerHelpers
from apiautotest.src.Utilities.requestUtilities import RequestUtility
from apiautotest.src.dao.customers_dao import Customer_DAO
import pdb

@pytest.mark.customer
@pytest.mark.smoke
@pytest.mark.tcid29
def test_create_customer():
    logger.info("TEST: Create new customer with email & pass")

    rand_info = generate_rand_email_and_pass()
    logger.info(rand_info)

    email=rand_info['email']
    password=rand_info['password']

   # Create Payload
    payload = {'email': email, 'password': password}

   # Make the call
    cust_obj=CustomerHelpers()
    cust_obj_api=CustomerHelpers.create_customers(self=None, email=email, password=password)

    # Verfiy email and first name in the response
    assert cust_obj_api['email'] == email, f"Create customer api return wrong email, Email: {email}"
    assert cust_obj_api['first_name'] == '', f"Create customer api return value of the first name"

    cust_dao= Customer_DAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_obj_api['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in DB.' \
                                  f'Email: {email}'


@pytest.mark.customer
@pytest.mark.tcid47
def test_create_customer_with_existing_user():

    # Get existing email from db
    cust_dao= Customer_DAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email= existing_cust[0]['user_email']

    # Make the API call
    req_help = RequestUtility()
    payload= {"email": existing_email, "password" : "pass123"}
    cust_obj_api = req_help.apost(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_obj_api['code'] == 'registration-error-email-exists', f"Create customer with" \
    f"existing user error 'code' is not correct. Expected: 'registration-error-email-exists'," \
    f"Actual: {cust_obj_api['code']}"

    assert cust_obj_api['message'] == 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>', \
    f"Create customer with existing user error 'message' is not correct. " \
    f"Expected: 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>'," \
    f"Actual: {cust_obj_api['message']}"
