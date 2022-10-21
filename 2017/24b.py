from typing import List

input = """14/42
2/3
6/44
4/10
23/49
35/39
46/46
5/29
13/20
33/9
24/50
0/30
9/10
41/44
35/50
44/50
5/11
21/24
7/39
46/31
38/38
22/26
8/9
16/4
23/39
26/5
40/40
29/29
5/20
3/32
42/11
16/14
27/49
36/20
18/39
49/41
16/6
24/46
44/48
36/4
6/6
13/6
42/12
29/41
39/39
9/3
30/2
25/20
15/6
15/23
28/40
8/7
26/23
48/10
28/28
2/13
48/14"""

#
# input = """0/2
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
for line in input.splitlines():
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
        if len(new_path) > len(best_path):
            current_strength = get_strength(new_path)
            best_path = new_path
        elif len(new_path) == len(best_path):
            if get_strength(new_path) > current_strength:
                current_strength = get_strength(new_path)
                best_path = new_path

    return best_path

print(get_strength(build_path([], connectors)))




