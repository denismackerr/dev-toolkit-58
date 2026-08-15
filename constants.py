import time
import random

def retry_operation(max_retries=3, delay=2, backoff=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    sleep_time = delay * (backoff ** (retries - 1)) + random.uniform(0, 1)
                    time.sleep(sleep_time)
            raise Exception(f'Operation failed after {max_retries} retries')
        return wrapper
    return decorator
