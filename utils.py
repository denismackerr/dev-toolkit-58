import json
import requests

API_URL = 'https://api.coingecko.com/api/v3/'


def fetch_crypto_data(crypto_id):
    response = requests.get(f'{API_URL}coins/markets', params={'vs_currency': 'usd', 'ids': crypto_id})
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def get_price(crypto_data):
    if crypto_data and isinstance(crypto_data, list):
        return crypto_data[0].get('current_price')
    return None


def convert_to_json(data):
    try:
        return json.dumps(data, indent=4)
    except (TypeError, OverflowError):
        return None


def display_crypto_info(crypto_id):
    data = fetch_crypto_data(crypto_id)
    price = get_price(data)
    if price:
        print(f'The current price of {crypto_id} is ${price}.')
    else:
        print('Data not available.')