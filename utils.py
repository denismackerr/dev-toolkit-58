import json


def load_json(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def flatten_list(nested_list: list) -> list:
    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flat_list.extend(flatten_list(sublist))
        else:
            flat_list.append(sublist)
    return flat_list


def chunk_list(input_list: list, chunk_size: int) -> list:
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]


def generate_uuid() -> str:
    import uuid
    return str(uuid.uuid4())