import re

def validate_address(address):
    pattern = r'^[0-9a-zA-Z]{34}$'
    if not re.match(pattern, address):
        raise ValueError('Invalid address format')


def validate_amount(amount):
    if amount <= 0:
        raise ValueError('Amount must be greater than zero')


def validate_inputs(address, amount):
    validate_address(address)
    validate_amount(amount)
