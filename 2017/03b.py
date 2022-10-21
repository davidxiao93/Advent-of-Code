input = """325489"""

input = int(input)

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def get_distance_squared(p: Point):
    return p.x * p.x + p.y * p.y

def add_point(p: Point, q:Point):
    return Point(x=p.x+q.x, y=p.y+q.y)


current_pos = Point(x=1,y=1)
grid = {
    Point(x=0, y=0): 1,
    Point(x=1, y=0): 1,
    Point(x=1, y=1): 2
}

up = Point(x=0, y=1)
down = Point(x=0, y=-1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

up_left = add_point(up, left)
up_right = add_point(up, right)
down_left = add_point(down, left)
down_right = add_point(down, right)

traverse_directions = {up, down, left, right}
sum_directions = {up_left, up, up_right, right, down_right, down, down_left, left}



while grid[current_pos] < input:
    # pick next point to go to
    possible_next_pos = [add_point(current_pos, t) for t in traverse_directions
                         if add_point(current_pos, t) not in grid]
    possible_next_pos.sort(key=lambda np: get_distance_squared(np))
    next_pos = possible_next_pos[0]
    s = sum([grid[add_point(next_pos, sd)] for sd in sum_directions
             if add_point(next_pos, sd) in grid])
    grid[next_pos] = s
    current_pos = next_pos


print(grid[current_pos])


