import json

class CryptoError(Exception):
    pass


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise CryptoError('File not found: {}'.format(file_path))
    except json.JSONDecodeError:
        raise CryptoError('Error decoding JSON from file: {}'.format(file_path))


def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise CryptoError('IO error while saving file: {}'.format(file_path))


def calculate_percentage_change(old_value, new_value):
    if old_value == 0:
        raise CryptoError('Old value cannot be zero for percentage calculation')
    return ((new_value - old_value) / old_value) * 100


def validate_address(address):
    if len(address) != 42 or not address.startswith('0x'):
        raise CryptoError('Invalid address format')
    return True