import re

def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None


def validate_positive_integer(value):
    try:
        ivalue = int(value)
        return ivalue > 0
    except ValueError:
        return False


def validate_input(data):
    if not isinstance(data, dict):
        return False
    return all([
        validate_email(data.get('email', '')),  
        validate_positive_integer(data.get('age', 0))
    ])

