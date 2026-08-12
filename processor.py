import requests
import json

class CryptoProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
            return None
        except json.JSONDecodeError as json_err:
            print(f'JSON decode error: {json_err}')
            return None
        except Exception as err:
            print(f'An error occurred: {err}')
            return None

    def process_data(self, data):
        if not data:
            raise ValueError('No data provided')
        # Process data as needed
        return data['prices']

if __name__ == '__main__':
    processor = CryptoProcessor('https://api.example.com/crypto')
    data = processor.fetch_data()
    if data:
        processed = processor.process_data(data)
        print(processed)