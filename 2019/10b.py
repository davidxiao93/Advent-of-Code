
import file_loader

input_string = file_loader.get_input()



from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
asteroids = []
for y, row in enumerate(input_string.splitlines()):
    for x, c in enumerate(row):
        if c == "#":
            asteroids.append(Point(x, y))

def get_offset(a: Point, b: Point) -> Point:
    dx = b.x - a.x
    dy = b.y - a.y
    if dx == 0 and dy == 0:
        return Point(0, 0)
    if dx == 0 and dy < 0:
        return Point(0, -1)
    if dx == 0 and dy > 0:
        return Point(0, 1)
    if dy == 0 and dx > 0:
        return Point(1, 0)
    if dy == 0 and dx < 0:
        return Point(-1, 0)
    for d in range(min(abs(dx), abs(dy)), 0, -1):
        # yes i know that going through every value is inefficient. so what
        if dx % d == 0 and dy % d == 0:
            dx = dx // d
            dy = dy // d
    return Point(dx, dy)

best_count = 0
laser_pos = None
for a in asteroids:
    seen_directions = set()
    for b in asteroids:
        if a == b:
            continue
        offset = get_offset(a, b)
        if offset not in seen_directions:
            seen_directions.add(offset)
    if len(seen_directions) > best_count:
        best_count = len(seen_directions)
        laser_pos = a

assert(laser_pos is not None)

asteroids.remove(laser_pos)

destroyed = 0
while destroyed < 200:
    seen_directions = {}
    for b in asteroids:
        offset = get_offset(laser_pos, b)
        if offset not in seen_directions:
            seen_directions[offset] = b
    asteroids_to_destroy = [ # get asteroids facing exactly up
        b
        for o, b in seen_directions.items()
        if o.x == 0 and o.y < 0
    ] + [ # get asteroids facing rightwards
        b
        for o, b in sorted(
            [(o, b) for o, b in seen_directions.items() if o.x > 0],
            key=lambda e: e[0].y / e[0].x
        )
    ] + [ # get asteroids facing exactly down
        b
        for o, b in seen_directions.items()
        if o.x == 0 and o.y > 0
    ] + [ # get asteroids facing leftwards
        b
        for o, b in sorted(
            [(o, b) for o, b in seen_directions.items() if o.x < 0],
            key=lambda e: e[0].y / e[0].x
        )
    ]
    for a in asteroids_to_destroy:
        asteroids.remove(a)
        destroyed += 1
        if destroyed == 200:
            print(a.x * 100 + a.y)





