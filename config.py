import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filepath):
            raise ConfigError(f'Config file not found: {self.filepath}')
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(f'Error decoding JSON: {e}')

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.data, f, indent=4)
        except IOError as e:
            raise ConfigError(f'Error saving config: {e}')

config = Config('config.json')
