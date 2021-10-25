
import logging as logger
import random
import string

def generate_rand_email_and_pass(sdomain=None, email_prefix=None):
    logger.debug("Generate random email address")

    if not domain:
         domain = 'supersqa.com'
    if not email_prefix:
         email_prefix = 'testuser'

    random_email_string_length=10
    random_string=''.join(random.choices(string.ascii_lowercase,k=random_email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain

    random_pass_string_length=20
    passw=''.join(random.choices(string.ascii_letters,k=random_pass_string_length))

    random_info= {'email':email, 'password':passw};
    logger.debug("Randomly generating email and password:"+ {random_info})

    return random_info
