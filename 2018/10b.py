from typing import List

import file_loader

input_string = file_loader.get_input()


# input_string = """position=<     9,      1> velocity=< 0,  2>
# position=<     7,      0> velocity=<-1,  0>
# position=<     3,     -2> velocity=<-1,  1>
# position=<     6,     10> velocity=<-2, -1>
# position=<     2,     -4> velocity=< 2,  2>
# position=<    -6,     10> velocity=< 2, -2>
# position=<     1,      8> velocity=< 1, -1>
# position=<     1,      7> velocity=< 1,  0>
# position=<    -3,     11> velocity=< 1, -2>
# position=<     7,      6> velocity=<-1, -1>
# position=<    -2,      3> velocity=< 1,  0>
# position=<    -4,      3> velocity=< 2,  0>
# position=<    10,     -3> velocity=<-1,  1>
# position=<     5,     11> velocity=< 1, -2>
# position=<     4,      7> velocity=< 0, -1>
# position=<     8,     -2> velocity=< 0,  1>
# position=<    15,      0> velocity=<-2,  0>
# position=<     1,      6> velocity=< 1,  0>
# position=<     8,      9> velocity=< 0, -1>
# position=<     3,      3> velocity=<-1,  1>
# position=<     0,      5> velocity=< 0, -1>
# position=<    -2,      2> velocity=< 2,  0>
# position=<     5,     -2> velocity=< 1,  2>
# position=<     1,      4> velocity=< 2,  1>
# position=<    -2,      7> velocity=< 2, -2>
# position=<     3,      6> velocity=<-1, -1>
# position=<     5,      0> velocity=< 1,  0>
# position=<    -6,      0> velocity=< 2,  0>
# position=<     5,      9> velocity=< 1, -2>
# position=<    14,      7> velocity=<-2,  0>
# position=<    -3,      6> velocity=< 2, -1>"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

class Star:
    def __init__(self, initial_pos: Point, velocity: Point):
        self.pos = initial_pos
        self.vel = velocity

    def advance(self):
        self.pos = Point(x=self.pos.x + self.vel.x, y=self.pos.y + self.vel.y)

    def rewind(self):
        self.pos = Point(x=self.pos.x - self.vel.x, y=self.pos.y - self.vel.y)

def get_bounds(stars: List[Star]):
    left_bound = stars[0].pos.x
    right_bound = stars[0].pos.x
    up_bound = stars[0].pos.y
    down_bound = stars[0].pos.y
    for s in stars:
        if s.pos.x < left_bound:
            left_bound = s.pos.x
        if s.pos.x > right_bound:
            right_bound = s.pos.x
        if s.pos.y > up_bound:
            up_bound = s.pos.y
        if s.pos.y < down_bound:
            down_bound = s.pos.y
    return up_bound, down_bound, left_bound, right_bound

def get_bound_area(stars: List[Star]):
    up_bound, down_bound, left_bound, right_bound = get_bounds(stars)
    return (up_bound - down_bound) * (right_bound - left_bound)

def pretty_print(stars: List[Star]):
    up_bound, down_bound, left_bound, right_bound = get_bounds(stars)
    rows = []
    for i in range(up_bound - down_bound + 1):
        rows.append(["."] * (right_bound - left_bound + 1))
    for s in stars:
        rows[s.pos.y - down_bound][s.pos.x - left_bound] = "#"
    for row in rows:
        print("".join(row))


stars = []
for line in input_string.splitlines():
    stars.append(
        Star(
            initial_pos = Point(
                x = int(line[10:16]),
                y = int(line[17:24])
            ),
            velocity = Point(
                x = int(line[36:38]),
                y = int(line[39:42])
            )
        )
    )

last_bound_area = get_bound_area(stars)
time_spent = 0
while True:
    for s in stars:
        s.advance()
    time_spent += 1
    new_bound_area = get_bound_area(stars)
    if new_bound_area > last_bound_area:
        for s in stars:
            s.rewind()
        time_spent -= 1
        print(time_spent)
        break
    last_bound_area = new_bound_area

exit(0)


