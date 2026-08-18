import json
import requests

class CryptoData:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self, endpoint):
        response = requests.get(f'{self.base_url}{endpoint}')
        if response.status_code != 200:
            raise ValueError('Failed to fetch data')
        return response.json()

    def process_data(self, data):
        return { 'price': data['price'], 'timestamp': data['timestamp'] }

    def get_crypto_price(self, crypto_symbol):
        endpoint = f'/price/{crypto_symbol}'
        data = self.fetch_data(endpoint)
        return self.process_data(data)