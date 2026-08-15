import json

class InputValidationError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, dict):
        raise InputValidationError('Input must be a dictionary')
    if 'amount' not in data or not isinstance(data['amount'], (int, float)):
        raise InputValidationError('Input must contain a numeric amount')
    if 'currency' not in data or not isinstance(data['currency'], str):
        raise InputValidationError('Input must contain a valid currency string')

def process_transaction(data):
    validate_input(data)
    amount = data['amount']
    currency = data['currency']
    result = f'Transaction of {amount} {currency} processed'
    return result

if __name__ == '__main__':
    raw_data = input('Enter transaction data as JSON: ')
    try:
        data = json.loads(raw_data)
        result = process_transaction(data)
        print(result)
    except InputValidationError as e:
        print(f'Input validation error: {e}')
    except json.JSONDecodeError:
        print('Invalid JSON input')
