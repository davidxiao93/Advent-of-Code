import file_loader

input_string = file_loader.get_input()

from collections import namedtuple

Point = namedtuple("Point", ["id", "x", "y"])

points = set()
for id, line in enumerate(input_string.splitlines()):
    words = line.split(",")
    x, y = [int(a) for a in words]
    points.add(Point(id, x, y))

# get bounds

a_point = next(iter(points))
left_bound = a_point.x
right_bound = a_point.x
up_bound = a_point.y
down_bound = a_point.y

for p in points:
    if p.x < left_bound:
        left_bound = p.x
    if p.x > right_bound:
        right_bound = p.x
    if p.y < up_bound:
        up_bound = p.y
    if p.y > down_bound:
        down_bound = p.y

# Find closest points within the bounds
# Anything outside the bounds is uninteresting as it just leads off into infinite space
def distance(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)


def find_closest(p, points):
    closest_dist = None
    closest = set()
    for q in points:
        dist = distance(p, q)
        if closest_dist == None or dist < closest_dist:
            closest = {q.id}
            closest_dist = dist
        elif dist == closest_dist:
            closest.add(q.id)
    return closest

grid = [
    [0] * (right_bound - left_bound + 1) for i in range(down_bound - up_bound + 1)
]

for y in range(up_bound, down_bound + 1):
    for x in range(left_bound, right_bound + 1):
        closest_points = find_closest(Point(id=None, x=x, y=y), points)
        if len(closest_points) > 1:
            grid[y-up_bound][x-left_bound] = -1
        elif len(closest_points) == 0:
            print("wtf")
            exit(1)
        else:
            grid[y - up_bound][x - left_bound] = closest_points.pop()

# We have our grid, we can remove any point ids that lie on the edge as they
# will continue off to infinity
candidate_ids = {p.id for p in points}

for y in [0, down_bound - up_bound]:
    for x in [0, right_bound - left_bound]:
        if grid[y][x] in candidate_ids:
            candidate_ids.remove(grid[y][x])

# we have our contenders
# now find which has the smallest finite space
ids_to_count = {}
for y in range(0, down_bound - up_bound + 1):
    for x in range(0, right_bound - left_bound + 1):
        if grid[y][x] in candidate_ids:
            if grid[y][x] not in ids_to_count:
                ids_to_count[grid[y][x]] = 0
            ids_to_count[grid[y][x]] += 1

print(max(ids_to_count.values()))




