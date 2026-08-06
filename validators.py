import re

def validate_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_username(username: str) -> bool:
    return 3 <= len(username) <= 30 and username.isalnum()


def validate_age(age: int) -> bool:
    return 0 <= age <= 120


def validate_input(data: dict) -> dict:
    errors = {}
    if not validate_email(data.get('email', '')):
        errors['email'] = 'Invalid email format.'
    if not validate_username(data.get('username', '')):
        errors['username'] = 'Username must be 3-30 characters long and alphanumeric.'
    if not validate_age(data.get('age', -1)):
        errors['age'] = 'Age must be between 0 and 120.'
    return errors
