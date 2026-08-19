import json

class CryptoError(Exception):
    pass

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise CryptoError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise CryptoError(f"Invalid JSON in file: {file_path}")

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        raise CryptoError(f"Failed to write to {file_path}: {str(e)}")

def validate_address(address):
    if not isinstance(address, str) or len(address) != 42:
        raise CryptoError(f"Invalid address format: {address}")
    return True

def convert_to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        raise CryptoError(f"Cannot convert {value} to float")