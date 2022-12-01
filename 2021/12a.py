from typing import List, Dict

import file_loader

input_string = file_loader.get_input()

neighbours: Dict[str, List[str]] = dict()

for line in input_string.splitlines():
    n1, n2 = line.split("-", 2)
    if n1 not in neighbours:
        neighbours[n1] = []
    neighbours[n1].append(n2)
    if n2 not in neighbours:
        neighbours[n2] = []
    neighbours[n2].append(n1)


def find_paths(current_path: List[str]) -> List[List[str]]:
    last_cave = current_path[-1]
    if last_cave == "end":
        return [current_path]
    next_caves = [n
                  for n in neighbours[last_cave]
                  if n.lower() != n # big cave
                  or n not in current_path # small cave but not yet visited
                  ]
    paths = []
    for n in next_caves:
        paths += find_paths(current_path + [n])
    return paths

paths = find_paths(["start"])

print(len(paths))
