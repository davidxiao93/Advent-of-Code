from typing import List

import file_loader

input_string = file_loader.get_input()
steps = 1000


from collections import namedtuple
Point = namedtuple("Point", ["x", "y", "z"])
def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y, p.z + q.z)

class Moon:
    def __init__(self, position: Point):
        self.position = position
        self.velocity = Point(0,0,0)

moons: List[Moon] = []
for line in input_string.splitlines():
    x, y, z = [
        int(x.split("=")[-1]) for x in line[1:-1].split(",")
    ]
    moons.append(Moon(Point(x, y, z)))

from itertools import combinations

def get_gravity(m: Moon, n: Moon, l):
    if l(m.position) < l(n.position):
        return 1
    elif l(m.position) > l(n.position):
        return -1
    else:
        return 0

for i in range(steps):
    # Update velocities with gravity
    for m, n in combinations(moons, 2):
        m_to_n_gravity = Point(
            get_gravity(m, n, lambda p: p.x),
            get_gravity(m, n, lambda p: p.y),
            get_gravity(m, n, lambda p: p.z),
        )
        n_to_m_gravity = Point(-1 * m_to_n_gravity.x, -1 * m_to_n_gravity.y, -1 * m_to_n_gravity.z)
        m.velocity = add_point(m.velocity, m_to_n_gravity)
        n.velocity = add_point(n.velocity, n_to_m_gravity)
    # update position
    for m in moons:
        m.position = add_point(m.position, m.velocity)

def pretty_print(moons: List[Moon]):
    for m in moons:
        print(m.position, m.velocity)


def get_energy_of_moon(m: Moon) -> int:
    return (abs(m.position.x) + abs(m.position.y) + abs(m.position.z)) \
         * (abs(m.velocity.x) + abs(m.velocity.y) + abs(m.velocity.z))

print(sum([get_energy_of_moon(m) for m in moons]))