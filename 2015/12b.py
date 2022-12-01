import file_loader

input_string = file_loader.get_input()

import json

j = json.loads(input_string)

def parse_json(j):
    if isinstance(j, list):
        partial_count = 0
        for k in j:
            partial_count += parse_json(k)
        return partial_count
    if isinstance(j, dict):
        if "red" in j.values():
            return 0
        partial_count = 0
        for key, value in j.items():
            partial_count += parse_json(key)
            partial_count += parse_json(value)
        return partial_count
    if isinstance(j, int):
        return int(j)
    if isinstance(j, str):
        return 0

print(parse_json(j))
