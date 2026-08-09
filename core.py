import logging

class App:
    def __init__(self, name):
        self.name = name
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger(self.name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def run(self):
        self.logger.info('Application is starting')
        try:
            self.process_data()
        except Exception as e:
            self.logger.error('An error occurred: %s', e)

    def process_data(self):
        self.logger.info('Processing data...')
        # Simulating data processing logic
        result = self.calculate()
        self.logger.info('Data processed successfully: %s', result)

    def calculate(self):
        # Placeholder calculation logic
        return 42

if __name__ == '__main__':
    app = App('MyApp')
    app.run()