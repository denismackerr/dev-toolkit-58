from typing import List, Dict, Any

class CryptoAnalyzer:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = data

    def calculate_average_price(self) -> float:
        total_price = sum(item['price'] for item in self.data)
        return total_price / len(self.data) if self.data else 0.0

    def get_top_n_coins(self, n: int) -> List[Dict[str, Any]]:
        return sorted(self.data, key=lambda x: x['market_cap'], reverse=True)[:n]

    def filter_by_min_volume(self, min_volume: float) -> List[Dict[str, Any]]:
        return [item for item in self.data if item['volume'] >= min_volume]