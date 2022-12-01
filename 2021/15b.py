from typing import Tuple, Dict, List, Set

import file_loader

input_string = file_loader.get_input()

import file_loader

input_string = file_loader.get_input()

risk_levels = dict()
for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        for a in range(5):
            for b in range(5):
                r = (int(c) + a + b)
                while r > 9:
                    r -= 9
                risk_levels[(x + len(input_string.splitlines()[0])*a, y + len(input_string.splitlines())*b)] = r

max_y = len(input_string.splitlines())*5 - 1
max_x = len(input_string.splitlines()[0])*5 - 1

# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         print(risk_levels[(x, y)], end="")
#     print("")

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

summed_risks = {
    (0,0): 0
}

points_to_check: Dict[int, Set[Tuple[int, int]]] = {
    0: {(0,0)}
}

while True:

    current_risk = min(points_to_check.keys())

    next_point_to_check = points_to_check[current_risk].pop()

    if len(points_to_check[current_risk]) == 0:
        del points_to_check[current_risk]

    if next_point_to_check == (max_x, max_y):
        print(current_risk)
        exit()

    for d in directions:
        to_check = (next_point_to_check[0] + d[0], next_point_to_check[1] + d[1])
        if to_check in risk_levels:
            to_check_risk = current_risk + risk_levels[to_check]
            if to_check not in summed_risks or summed_risks[to_check] > to_check_risk:

                if to_check_risk not in points_to_check:
                    points_to_check[to_check_risk] = set()
                points_to_check[to_check_risk].add(to_check)
                summed_risks[to_check] = to_check_risk

