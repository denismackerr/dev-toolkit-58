import logging
import time

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def retry(func):
        def wrapper(*args, **kwargs):
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts - 1:
                        time.sleep(2 ** attempt)
                    else:
                        raise e
        return wrapper

    @retry
    def perform_network_operation(self):
        # Simulated network operation
        raise ConnectionError('Simulated network failure')

logger = Logger(__name__)
try:
    logger.perform_network_operation()
except Exception as ex:
    logger.error(f'Operation failed: {ex}')