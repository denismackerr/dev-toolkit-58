import re

def is_valid_address(address: str) -> bool:
    pattern = r'^0x[0-9a-fA-F]{40}$'
    return bool(re.match(pattern, address))


def is_valid_amount(amount: float) -> bool:
    return amount > 0


def is_valid_transaction(data: dict) -> bool:
    return all(key in data for key in ('from', 'to', 'amount')) and \
           is_valid_address(data['from']) and \
           is_valid_address(data['to']) and \
           is_valid_amount(data['amount'])


def validate_transactions(transactions: list) -> list:
    return [tx for tx in transactions if is_valid_transaction(tx)]


def extract_addresses(transactions: list) -> set:
    addresses = set()
    for tx in transactions:
        addresses.add(tx['from'])
        addresses.add(tx['to'])
    return addresses