import re

class ValidationError(Exception):
    pass

def validate_email(email: str) -> None:
    if not isinstance(email, str):
        raise ValidationError('Email must be a string')
    if len(email) == 0:
        raise ValidationError('Email cannot be empty')
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', email):
        raise ValidationError('Invalid email format')

def validate_age(age: int) -> None:
    if not isinstance(age, int):
        raise ValidationError('Age must be an integer')
    if age < 0:
        raise ValidationError('Age cannot be negative')
    if age > 120:
        raise ValidationError('Age is unrealistic')

def validate_username(username: str) -> None:
    if not isinstance(username, str):
        raise ValidationError('Username must be a string')
    if len(username) < 3 or len(username) > 20:
        raise ValidationError('Username must be between 3 and 20 characters')
    if not re.match(r'^[\w]+$', username):
        raise ValidationError('Username can only contain alphanumeric characters and underscores')