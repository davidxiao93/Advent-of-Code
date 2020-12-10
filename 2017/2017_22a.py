input = """.#...#.#.##..##....##.#.#
###.###..##...##.##....##
....#.###..#...#####..#.#
.##.######..###.##..#...#
#..#..#..##..###...#..###
..####...#.##.#.#.##.####
#......#..####..###..###.
#####.##.#.#.##.###.#.#.#
.#.###....###....##....##
.......########.#.#...#..
...###.####.##..###.##..#
#.#.###.####.###.###.###.
.######...###.....#......
....##.###..#.#.###...##.
#.###..###.#.#.##.#.##.##
#.#.#..###...###.###.....
##..##.##...##.##..##.#.#
.....##......##..#.##...#
..##.#.###.#...#####.#.##
....##..#.#.#.#..###.#..#
###..##.##....##.#....##.
#..####...####.#.##..#.##
####.###...####..##.#.#.#
#.#.#.###.....###.##.###.
.#...##.#.##..###.#.###.."""


# input = """..#
# #..
# ..."""


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

current_position = Point(x=0, y=0)
current_direction = 0
directions = [up, right, down, left]

def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)


infected = set()

lines = input.splitlines()
initial_grid_size = int((len(lines[0]) - 1)/2)
for y, r in enumerate(lines):
    for x, c in enumerate(r):
        if c == '#':
            infected.add(Point(x=x-initial_grid_size, y=y-initial_grid_size))


def pretty_print(infected, current_position, current_direction):
    for y in range(-5, 6):
        r = []
        for x in range(-5, 6):
            if Point(x, y) in infected:
                a = "#"
            else:
                a = "."
            if Point(x, y) == current_position:
                b = str(current_direction) + " "
            else:
                b = "  "
            r.append(a + b)
        print("".join(r))


infections_caused = 0
for i in range(10000):
    # pretty_print(infected, current_position, current_direction)
    # print("----")
    if current_position in infected:
        current_direction = (current_direction + 1) % 4
        infected.remove(current_position)
    else:
        current_direction = (current_direction - 1) % 4
        infections_caused += 1
        infected.add(current_position)
    current_position = add_point(current_position, directions[current_direction])

pretty_print(infected, current_position, current_direction)

print(infections_caused)