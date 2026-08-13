from typing import List

class TransactionProcessor:
    """
    Processes cryptocurrency transactions.
    """

    def __init__(self, fee_percentage: float) -> None:
        """
        Initializes the transaction processor with a fee percentage.
        """        
        self.fee_percentage = fee_percentage

    def calculate_fee(self, amount: float) -> float:
        """
        Calculates the fee for a given transaction amount.
        
        :param amount: The transaction amount.
        :return: The calculated fee.
        """        
        return amount * self.fee_percentage

    def process_transactions(self, transactions: List[float]) -> List[float]:
        """
        Processes a list of transaction amounts.
        
        :param transactions: A list of transaction amounts.
        :return: A list of fees for each transaction.
        """        
        return [self.calculate_fee(amount) for amount in transactions]

if __name__ == '__main__':
    processor = TransactionProcessor(0.01)
    fees = processor.process_transactions([100.0, 250.5, 75.25])
    print(fees)  # Output fees for the transactions