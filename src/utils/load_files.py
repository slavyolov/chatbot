import json


def load_json_file(filename):
    with open(filename) as f:
        file = json.load(f)
    return file
