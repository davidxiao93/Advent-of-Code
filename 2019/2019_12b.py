from typing import List, Callable, Tuple

input = """<x=4, y=1, z=1>
<x=11, y=-18, z=-1>
<x=-2, y=-10, z=-4>
<x=-7, y=-2, z=14>"""
steps = 1000000


from collections import namedtuple
Point = namedtuple("Point", ["x", "y", "z"])
def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y, p.z + q.z)


"""
observation: the x, y, z axis are all operating independent of each other
this means that I can look for the cycle in each of these axis rather than trying to find the 
cycle for all three at the same time
"""





class Moon:
    def __init__(self, position: Point):
        self.position = position
        self.velocity = Point(0,0,0)

moons: List[Moon] = []
for line in input.splitlines():
    x, y, z = [
        int(x.split("=")[-1]) for x in line[1:-1].split(",")
    ]
    moons.append(Moon(Point(x, y, z)))

from itertools import combinations

def get_gravity(a: int, b: int) -> int:
    if a < b:
        return 1
    elif b < a:
        return -1
    else:
        return 0

def find_cycle_one_dim(moons: List[Moon], l: Callable[[Point], int]) -> Tuple[int, int]:
    # returns a tuple of (offset, cycle)
    moon_pos = [l(m.position) for m in moons]
    moon_vel = [l(m.velocity) for m in moons]
    seen_states = {}
    count = 0
    while True:
        state = tuple(moon_pos + moon_vel)
        if state in seen_states:
            return (seen_states[state], count - seen_states[state])
        seen_states[state] = count
        for m, n in combinations(range(len(moon_pos)), 2):
            m_to_n_gravity = get_gravity(moon_pos[m], moon_pos[n])
            moon_vel[m] += m_to_n_gravity
            moon_vel[n] -= m_to_n_gravity
        for m in range(len(moon_pos)):
            moon_pos[m] += moon_vel[m]
        count += 1

offset_x, loop_x = find_cycle_one_dim(moons, lambda p: p.x)
offset_y, loop_y = find_cycle_one_dim(moons, lambda p: p.y)
offset_z, loop_z = find_cycle_one_dim(moons, lambda p: p.z)

"""
luckily for me, all the offsets are 0, so the earliest time is the lowest common multiple
of loop_x, loop_y, loop_z
"""
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print(lcm(lcm(loop_x, loop_y), loop_z))




