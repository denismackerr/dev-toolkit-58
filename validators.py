import re

class Validator:
    @staticmethod
    def is_valid_address(address: str) -> bool:
        pattern = r'^(0x)?[0-9a-fA-F]{40}$'
        return bool(re.match(pattern, address))

    @staticmethod
    def is_valid_signature(signature: str) -> bool:
        pattern = r'^[0-9a-fA-F]{130}$'
        return bool(re.match(pattern, signature))

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount > 0

    @staticmethod
    def is_valid_transaction(tx: dict) -> bool:
        return all(
            [
                Validator.is_valid_address(tx.get('from')),
                Validator.is_valid_address(tx.get('to')),
                Validator.is_valid_amount(tx.get('amount')),
                Validator.is_valid_signature(tx.get('signature'))
            ]
        )