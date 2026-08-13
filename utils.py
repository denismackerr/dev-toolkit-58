import json
import requests
from datetime import datetime
def fetch_crypto_data(symbol, currency='USD'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={currency}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
def format_crypto_data(data):
    if not data:
        return None
    formatted_data = {}
    for key, value in data.items():
        formatted_data[key] = {
            'price': value.get('usd'),
            'timestamp': datetime.utcnow().isoformat()
        }
    return formatted_data

def save_data_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)