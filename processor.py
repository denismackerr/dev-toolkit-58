import json
import requests
from requests.exceptions import RequestException

class CryptoProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            return {'error': str(e)}
        except json.JSONDecodeError:
            return {'error': 'Invalid JSON response'}

    def process_data(self, data):
        if 'error' in data:
            return data
        # Process valid data
        return {'processed_data': data}

    def run(self):
        data = self.fetch_data()
        result = self.process_data(data)
        return result

if __name__ == '__main__':
    processor = CryptoProcessor('https://api.example.com/crypto')
    print(processor.run())