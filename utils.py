import json
import requests

def fetch_crypto_data(symbol, vs_currency='usd'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={vs_currency}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def format_crypto_data(data):
    formatted_data = {
        'symbol': data['id'],
        'price': data['usd'],
    }
    return json.dumps(formatted_data, indent=4)


def save_to_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data)


def load_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()