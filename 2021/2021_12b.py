from typing import List, Dict

input = """yb-pi
jg-ej
yb-KN
LD-start
end-UF
UF-yb
yb-xd
qx-yb
xd-end
jg-KN
start-qx
start-ej
qx-LD
jg-LD
xd-LD
ej-qx
end-KN
DM-xd
jg-yb
ej-LD
qx-UF
UF-jg
qx-jg
xd-UF"""

neighbours: Dict[str, List[str]] = dict()

for line in input.splitlines():
    n1, n2 = line.split("-", 2)
    if n1 not in neighbours:
        neighbours[n1] = []
    neighbours[n1].append(n2)
    if n2 not in neighbours:
        neighbours[n2] = []
    neighbours[n2].append(n1)


def can_visit_small_cave_again(current_path, next_cave):
    if next_cave == "start" or next_cave == "end":
        return False
    visited_small_caves = [c for c in current_path if c.lower() == c]
    return len(visited_small_caves) == len(set(visited_small_caves))


def find_paths(current_path: List[str]) -> List[List[str]]:
    last_cave = current_path[-1]
    if last_cave == "end":
        return [current_path]
    next_caves = [n
                  for n in neighbours[last_cave]
                  if n.lower() != n # big cave
                  or n not in current_path # small cave but not yet visited
                  or can_visit_small_cave_again(current_path, n)
                  ]
    paths = []
    for n in next_caves:
        paths += find_paths(current_path + [n])
    return paths

paths = find_paths(["start"])

print(len(paths))
