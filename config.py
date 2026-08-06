import json
import os

DEFAULT_CONFIG = {
    'setting1': 'default_value1',
    'setting2': 'default_value2',
    'setting3': 10,
}

def load_config(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            try:
                custom_config = json.load(file)
            except json.JSONDecodeError:
                return DEFAULT_CONFIG
        return {**DEFAULT_CONFIG, **custom_config}
    return DEFAULT_CONFIG
