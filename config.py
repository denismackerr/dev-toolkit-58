import json
import os

class ConfigLoader:
    def __init__(self, config_file='config.json', defaults=None):
        self.config_file = config_file
        self.defaults = defaults or {}
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            return self.defaults
        with open(self.config_file, 'r') as file:
            config_data = json.load(file)
        return {**self.defaults, **config_data}

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)