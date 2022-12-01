from __future__ import annotations
from collections import namedtuple
from itertools import combinations
from typing import List, Set, Tuple, Optional
import math

import file_loader

input_string = file_loader.get_input()

# input_string = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
# p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
# p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
# p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""



Point = namedtuple("Point", ["x", "y", "z"])

class Particle:
    def __init__(self, id, p, v, a):
        self.id = id
        self.p = p
        self.v = v
        self.a = a

    def __get_s(self, p, v, a, t):
        return int(p + t * (v + (0.5*a)) + 0.5 * a * t * t)

    def get_position_at_time(self, t):
        return Point(
            x = self.__get_s(self.p.x, self.v.x, self.a.x, t),
            y = self.__get_s(self.p.y, self.v.y, self.a.y, t),
            z = self.__get_s(self.p.z, self.v.z, self.a.z, t)
        )

    def collides_dimension(self, p: Particle, l):
        # Returns none if always colliding
        # Returns empty set if no collisions
        if l(self.a) == l(p.a):
            if l(self.v) == l(p.v):
                if l(self.p) == l(p.p):
                    return None
                else:
                    return set()
            else:
                ret = {
                    (l(self.p) - l(p.p))/(l(p.v) - l(self.v))
                }

        else:
            # quadratic
            a = (l(self.a) - l(p.a)) / 2
            b = l(self.v) - l(p.v) + a
            c = l(self.p) - l(p.p)
            quotient = (b ** 2) - (4 * a * c)
            if quotient < 0:
                return set()
            r = math.sqrt(quotient)
            ret = {
                (-1 * b + r) / (2 * a),
                (-1 * b - r) / (2 * a)
            }
        # return ret
        return {int(f) for f in ret if f.is_integer() and f >= 0}

    def collides(self, p: Particle) -> Set[int]:
        # returns list of times if there are collisions
        tx = self.collides_dimension(p, lambda point: point.x)
        ty = self.collides_dimension(p, lambda point: point.y)
        tz = self.collides_dimension(p, lambda point: point.z)
        sets = [s for s in [tx, ty, tz] if s is not None]
        ret = set.intersection(*sets)
        if len(ret) > 0:
            x = ret.copy().pop()
            if self.get_position_at_time(x) != p.get_position_at_time(x):
                print("invalid ??? coll", self.get_position_at_time(x), p.get_position_at_time(x))
        return ret


def to_point(s):
    ss = [int(x) for x in s.split(",")]
    return Point(ss[0], ss[1], ss[2])

particles = set()

for i, line in enumerate(input_string.splitlines()):
    pstr, vstr, astr = [s.strip()[3:-1] for s in line.split(", ")]
    particles.add(Particle(i, to_point(pstr), to_point(vstr), to_point(astr)))



def calc_earliest_collision(particles: Set[Particle]) -> Tuple[Optional[int], Optional[Point]]:
    earliest_collision_time = None
    earliest_collision_position = None
    for p, q in combinations(particles, 2):
        collisions = p.collides(q)
        if len(collisions) > 0:
            collision_time = min(collisions)
            if earliest_collision_time == None or collision_time < earliest_collision_time:
                earliest_collision_time = collision_time
                earliest_collision_position = p.get_position_at_time(earliest_collision_time)

    return earliest_collision_time, earliest_collision_position



collision_time, collision_position = calc_earliest_collision(particles)
while collision_time is not None:
    # print("Collides at t =", collision_time)
    particles_to_remove = set()
    for p in particles:
        if p.get_position_at_time(collision_time) == collision_position:
            particles_to_remove.add(p)
    # print("Removed", len(particles_to_remove))
    for p in particles_to_remove:
        particles.remove(p)
    # print("Remaining", len(particles))

    collision_time, collision_position = calc_earliest_collision(particles)

print(len(particles))