from typing import List


def calculate_average(prices: List[float]) -> float:
    """Calculate the average price from a list of prices."""
    return sum(prices) / len(prices) if prices else 0.0


def format_currency(amount: float, currency_symbol: str = '$') -> str:
    """Format the amount as a currency string."""
    return f'{currency_symbol}{amount:,.2f}'


def is_valid_address(address: str) -> bool:
    """Validate if the address is in a proper format."""
    return len(address) == 42 and address.startswith('0x')


def generate_transaction_id() -> str:
    """Generate a unique transaction ID."""
    import uuid
    return str(uuid.uuid4())


def parse_decimal(value: str) -> float:
    """Parse a decimal string into a float."""
    try:
        return float(value)
    except ValueError:
        return 0.0
