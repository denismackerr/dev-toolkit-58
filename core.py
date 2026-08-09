import json


def parse_json(data):
    """Parse a JSON string into a Python dictionary."""
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON data: {e}")


def serialize_to_json(obj, indent=None):
    """Convert a Python object to a JSON string."""
    try:
        return json.dumps(obj, indent=indent)
    except TypeError as e:
        raise ValueError(f"Object of type {type(obj).__name__} is not JSON serializable: {e}")


def flatten_dict(nested_dict, parent_key='', sep='_'):
    """Flatten a nested dictionary."""
    items = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_merge(dict1, dict2):
    """Merge two dictionaries recursively."""
    for key, value in dict2.items():
        if isinstance(value, dict) and key in dict1:
            dict1[key] = deep_merge(dict1[key], value)
        else:
            dict1[key] = value
    return dict1
