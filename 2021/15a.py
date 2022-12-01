from typing import Tuple, Dict, List, Set

import file_loader

input_string = file_loader.get_input()

risk_levels = dict()
for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        risk_levels[(x, y)] = int(c)

max_y = len(input_string.splitlines()) - 1
max_x = len(input_string.splitlines()[0]) - 1

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

summed_risks = {
    (0,0): 0
}

paths: Dict[int, Set[Tuple[Tuple[int, int], ...]]] = {
    0: {((0,0),)}
}

while True:

    current_risk = min(paths.keys())

    next_path_to_check = paths[current_risk].pop()

    if len(paths[current_risk]) == 0:
        del paths[current_risk]

    last_pos = next_path_to_check[-1]

    if last_pos == (max_x, max_y):
        print(current_risk)
        exit()

    for d in directions:
        to_check = (last_pos[0] + d[0], last_pos[1] + d[1])
        if to_check in risk_levels:
            to_check_risk = current_risk + risk_levels[to_check]
            if to_check not in summed_risks or summed_risks[to_check] > to_check_risk:

                if to_check_risk not in paths:
                    paths[to_check_risk] = set()
                paths[to_check_risk].add(
                    next_path_to_check + (to_check,)
                )
                summed_risks[to_check] = to_check_risk

