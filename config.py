import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.user_config = {}

    def load_config(self, filepath):
        try:
            with open(filepath, 'r') as file:
                self.user_config = json.load(file)
        except FileNotFoundError:
            self.user_config = {}
        except json.JSONDecodeError:
            self.user_config = {}

    def get_config(self):
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

if __name__ == '__main__':
    default = {'api_key': 'default_key', 'timeout': 30}
    config_loader = ConfigLoader(default)
    config_loader.load_config('config.json')
    current_config = config_loader.get_config()
    print(current_config)