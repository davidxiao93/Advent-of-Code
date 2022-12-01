from functools import reduce

import file_loader

input_string = file_loader.get_input()

points = dict()
for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        points[(x, y)] = int(c)

basin_sizes = []

while True:
    basin_seed = next((p for p, h in points.items() if h < 9), None)
    if basin_seed is None:
        # no more basins
        break

    basin = set()
    points_to_check = [basin_seed]
    not_basin = set()
    while len(points_to_check) > 0:
        p = points_to_check.pop(0)
        basin.add(p)
        for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            point_to_check = (p[0] + x, p[1] + y)
            if point_to_check in basin or point_to_check in not_basin:
                continue
            if points.get(point_to_check, 10) < 9:
                points_to_check.append(point_to_check)
            else:
                not_basin.add(point_to_check)
    basin_sizes.append(len(basin))
    for p in basin:
        del points[p]

print(
    reduce(
        lambda a, b: a*b,
        sorted(basin_sizes, reverse=True)[:3]
   )
)
