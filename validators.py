from typing import Any, Dict


def is_valid_address(address: str) -> bool:
    """Check if the provided address is a valid crypto address."""
    return len(address) == 42 and address.startswith('0x')


def validate_transaction(tx: Dict[str, Any]) -> bool:
    """Validate the structure of a transaction."""
    required_keys = {'from_address', 'to_address', 'amount', 'nonce'}
    return required_keys.issubset(tx.keys()) and \
           is_valid_address(tx['from_address']) and \
           is_valid_address(tx['to_address']) and \
           isinstance(tx['amount'], (int, float)) and \
           isinstance(tx['nonce'], int)


def is_valid_signature(signature: str) -> bool:
    """Check if the provided signature is valid."""
    return len(signature) == 128  # Example for a 64-byte hex signature


def validate_signature(tx: Dict[str, Any], signature: str) -> bool:
    """Validate the signature for a given transaction."""
    return is_valid_signature(signature)


def validate_all(tx: Dict[str, Any], signature: str) -> bool:
    """Validate the transaction and its signature."""
    return validate_transaction(tx) and validate_signature(tx, signature)