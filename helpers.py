import os
import shutil
import json

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def write_json_file(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def copy_file(source, destination):
    shutil.copy2(source, destination)


def delete_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)


def list_directory(path):
    return os.listdir(path)