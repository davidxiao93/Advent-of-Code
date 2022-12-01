from typing import List

import file_loader

input_string = file_loader.get_input()

#
# input_string = """0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10"""


from collections import namedtuple

Connector = namedtuple("Connector", ["a", "b"])

def get_dangling_connection(cs: List[Connector]):
    connection = 0
    for c in cs:
        if c.a == connection:
            connection = c.b
        elif c.b == connection:
            connection = c.a
    return connection


def get_strength(cs: List[Connector]):
    return sum([c.a + c.b for c in cs])


connectors = []
for line in input_string.splitlines():
    a, b = [int(x) for x in line.split("/")]
    connectors.append(Connector(a, b))


def build_path(current_path: List[Connector], remaining_connectors: List[Connector]):
    next_connector = get_dangling_connection(current_path)
    candidate_connectors = []
    for c in remaining_connectors:
        if c.a == next_connector or c.b == next_connector:
            candidate_connectors.append(c)

    current_strength = get_strength(current_path)
    best_path = current_path
    for c in candidate_connectors:
        new_current = current_path.copy() + [c]
        new_remaining = remaining_connectors.copy()
        new_remaining.remove(c)
        new_path = build_path(new_current, new_remaining)
        if get_strength(new_path) > current_strength:
            current_strength = get_strength(new_path)
            best_path = new_path

    return best_path

print(get_strength(build_path([], connectors)))




