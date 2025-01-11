import re


def is_valid_email(email):
    """
    Check if email is valid or not
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    else:
        return False
