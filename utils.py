import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def filter_dict(input_dict, keys):
    return {key: input_dict[key] for key in keys if key in input_dict}
