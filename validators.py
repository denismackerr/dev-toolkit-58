import re

class ValidationError(Exception):
    pass

class InputValidator:
    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise ValidationError('Email must be a string')
        if not re.match(r'^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$', email):
            raise ValidationError('Invalid email format')
        return True

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int):
            raise ValidationError('Age must be an integer')
        if age < 0:
            raise ValidationError('Age cannot be negative')
        return True

    @staticmethod
    def validate_username(username):
        if not isinstance(username, str):
            raise ValidationError('Username must be a string')
        if len(username) < 3 or len(username) > 20:
            raise ValidationError('Username must be between 3 and 20 characters')
        return True
