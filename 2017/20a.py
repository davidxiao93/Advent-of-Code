import file_loader

input_string = file_loader.get_input()



from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])

class Particle:
    def __init__(self, id, p, v, a):
        self.id = id
        self.p = p
        self.v = v
        self.a = a

def to_point(s):
    ss = [int(x) for x in s.split(",")]
    return Point(ss[0], ss[1], ss[2])

def distance(p: Point, q: Point):
    # using manhattan as that's what the question asks
    return abs(p.x - q.x) + abs(p.y - q.y) + abs(p.z - q.z)

particles = set()

for i, line in enumerate(input_string.splitlines()):
    pstr, vstr, astr = [s.strip()[3:-1] for s in line.split(", ")]
    particles.add(Particle(i, to_point(pstr), to_point(vstr), to_point(astr)))

# Closest particle in the long term will always be the one with the smallest acceleration
# If multiple particles have the same acceleration, then take the one with the smallest velocity
lowest_accelerating_particle = None
origin = Point(0,0,0)
for p in particles:
    if lowest_accelerating_particle is None:
        lowest_accelerating_particle = p
        continue

    if distance(origin, p.a) < distance(origin, lowest_accelerating_particle.a):
        lowest_accelerating_particle = p
    elif distance(origin, p.a) == distance(origin, lowest_accelerating_particle.a):
        if distance(origin, p.v) < distance(origin, lowest_accelerating_particle.v):
            lowest_accelerating_particle = p

print(lowest_accelerating_particle.id)

# 158 p=<696,2161,-2404>, v=<-35,-108,100>, a=<0,0,2>
# 243 p=<447,865,1300>, v=<-20,-39,-36>, a=<0,0,-2>