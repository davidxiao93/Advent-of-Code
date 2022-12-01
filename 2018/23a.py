import file_loader

input_string = file_loader.get_input()

from collections import namedtuple

Nanobot = namedtuple("Nanobot", ["x", "y", "z", "r"])

def distance(n: Nanobot, m: Nanobot):
    return abs(n.x - m.x) + abs(n.y - m.y) + abs(n.z - m.z)

nanobots = set()
strongest = None
for line in input_string.splitlines():
    pos_str, r_str = line.split(", ")
    r = int(r_str[2:])
    x, y, z = (int(a) for a in pos_str[5:-1].split(",", 2))
    n = Nanobot(x, y, z, r)
    nanobots.add(n)
    if strongest == None or n.r > strongest.r:
        strongest = n

in_range = 0
for n in nanobots:
    if distance(n, strongest) <= strongest.r:
        in_range += 1
print(in_range)