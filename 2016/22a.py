import file_loader

input_string = file_loader.get_input()

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

used_grid = {}
size_grid = {}

for line in input_string.splitlines()[2:]:
    words = line.split()
    _, x, y = words[0].rsplit("-", 2)
    x = int(x[1:])
    y = int(y[1:])
    size = int(words[1][:-1])
    used = int(words[2][:-1])
    p = Point(x, y)
    used_grid[p] = used
    size_grid[p] = size


def is_viable(p: Point, q:Point):
    return q in used_grid \
           and p in used_grid \
           and used_grid[p] != 0 \
           and p != q \
           and size_grid[q] - used_grid[q] >= used_grid[p]



from itertools import combinations

count = 0
pairs = combinations(set(size_grid.keys()), 2)
for p, q in pairs:
    if is_viable(p, q):
        count += 1
    if is_viable(q, p):
        count += 1

print(count)



# Turns out we dont just want viable pairs of connected nodes
# def add_point(p: Point, q:Point):
#     return Point(x=p.x+q.x, y=p.y+q.y)
#
# points_to_cover = {Point(x=0, y=0)}
#
# down = Point(x=0, y=1)
# up = Point(x=0, y=-1)
# left = Point(x=-1, y=0)
# right = Point(x=1, y=0)
#
# count = 0
# while len(points_to_cover) != 0:
#     next_point = points_to_cover.pop()
#     if next_point not in size_grid:
#         continue
#     right_point = add_point(next_point, right)
#     down_point = add_point(next_point, down)
#     points_to_cover.add(right_point)
#     points_to_cover.add(down_point)
#
#     if is_viable(next_point, right_point):
#         count += 1
#     if is_viable(right_point, next_point):
#         count += 1
#
#     if is_viable(next_point, down_point):
#         count += 1
#     if is_viable(down_point, next_point):
#         count += 1
#
#
#
#
# print(count)










