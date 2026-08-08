import re

def validate_input(input_value):
    if not isinstance(input_value, str):
        raise ValueError('Input must be a string.')
    if not input_value:
        raise ValueError('Input cannot be empty.')
    if len(input_value) > 100:
        raise ValueError('Input cannot exceed 100 characters.')
    if not re.match('^[a-zA-Z0-9 ]*$', input_value):
        raise ValueError('Input can only contain alphanumeric characters and spaces.')
    return True