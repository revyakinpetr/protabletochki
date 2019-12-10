import json


def get_json_from_file(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)
