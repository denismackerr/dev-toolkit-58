import json
import requests

class CryptoDataProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, crypto_symbol):
        response = requests.get(f'{self.api_url}/{crypto_symbol}')
        response.raise_for_status()
        return response.json()

    def process_data(self, data):
        return {
            'symbol': data['symbol'],
            'price': float(data['price']),
            'market_cap': int(data['market_cap']),
            'timestamp': data['timestamp']
        }

    def save_to_json(self, processed_data, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(processed_data, json_file, indent=4)

    def handle_crypto_data(self, crypto_symbol, output_file):
        raw_data = self.fetch_data(crypto_symbol)
        processed_data = self.process_data(raw_data)
        self.save_to_json(processed_data, output_file)

