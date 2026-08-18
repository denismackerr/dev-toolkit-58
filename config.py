import json
import os

class ConfigLoader:
    def __init__(self, config_path='config.json', defaults=None):
        self.config_path = config_path
        self.defaults = defaults or {}
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            return self.defaults
        with open(self.config_path, 'r') as file:
            return {**self.defaults, **json.load(file)}

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    default_config = {'api_key': 'default_key', 'timeout': 30}
    config_loader = ConfigLoader(defaults=default_config)
    api_key = config_loader.get('api_key')
    timeout = config_loader.get('timeout')
    print(api_key, timeout)