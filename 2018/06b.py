import file_loader

input_string = file_loader.get_input()
target = 10000


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x=0, y=1)
down = Point(x=0, y=-1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

def add_point(p, q):
    return Point(p.x+q.x, p.y+q.y)

points = set()
for line in input_string.splitlines():
    words = line.split(",")
    x, y = [int(a) for a in words]
    points.add(Point(x, y))


def distance(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)


def is_close(p, points, target):
    count = 0
    for q in points:
        count += distance(p, q)
        if count >= target:
            return False
    return True


# find center.
# The center will always have the lowest sum of spokes

center_x = int(sum([p.x for p in points]) / len(points))
center_y = int(sum([p.y for p in points]) / len(points))

# Then search outwards.
# The region that fulfils the criteria of being sufficient close to all points must be a single
# contiguous area.
matching = set()
candiates = {Point(center_x, center_y)}
while len(candiates) != 0:
    next_candidate = candiates.pop()

    if is_close(next_candidate, points, target):
        matching.add(next_candidate)
        for d in [up, down, left, right]:
            new_candidate = add_point(next_candidate, d)
            if new_candidate not in matching and new_candidate not in candiates:
                candiates.add(new_candidate)

print(len(matching))







