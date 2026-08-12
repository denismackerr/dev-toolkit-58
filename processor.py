import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            raise NetworkError(f'HTTP error occurred: {response.status_code}')
        except requests.exceptions.RequestException:
            if attempt < max_retries - 1:
                time.sleep(delay)
                continue
            raise NetworkError('Max retries exceeded')
    return None

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except NetworkError as ne:
        print(ne)