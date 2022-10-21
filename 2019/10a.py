
input = """#.#....#.#......#.....#......####.
#....#....##...#..#..##....#.##..#
#.#..#....#..#....##...###......##
...........##..##..##.####.#......
...##..##....##.#.....#.##....#..#
..##.....#..#.......#.#.........##
...###..##.###.#..................
.##...###.#.#.......#.#...##..#.#.
...#...##....#....##.#.....#...#.#
..##........#.#...#..#...##...##..
..#.##.......#..#......#.....##..#
....###..#..#...###...#.###...#.##
..#........#....#.....##.....#.#.#
...#....#.....#..#...###........#.
.##...#........#.#...#...##.......
.#....#.#.#.#.....#...........#...
.......###.##...#..#.#....#..##..#
#..#..###.#.......##....##.#..#...
..##...#.#.#........##..#..#.#..#.
.#.##..#.......#.#.#.........##.##
...#.#.....#.#....###.#.........#.
.#..#.##...#......#......#..##....
.##....#.#......##...#....#.##..#.
#..#..#..#...........#......##...#
#....##...#......#.###.#..#.#...#.
#......#.#.#.#....###..##.##...##.
......#.......#.#.#.#...#...##....
....##..#.....#.......#....#...#..
.#........#....#...#.#..#....#....
.#.##.##..##.#.#####..........##..
..####...##.#.....##.............#
....##......#.#..#....###....##...
......#..#.#####.#................
.#....#.#..#.###....##.......##.#."""

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
asteroids = []
for y, row in enumerate(input.splitlines()):
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
print(best_count)
