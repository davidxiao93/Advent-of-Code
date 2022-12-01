import file_loader

input_string = file_loader.get_input()

orbits = {}

for line in input_string.splitlines():
    l, r = line.split(")")
    orbits[r] = l

orbit_counts = {
    "COM": 0
}


def get_orbit_count(target):
    if target not in orbit_counts:
        orbit_counts[target] = 1 + get_orbit_count(orbits[target])
    return orbit_counts[target]


def get_total_orbit_counts():
    return sum([
        get_orbit_count(p)
        for p in orbits.keys()
    ])


print(get_total_orbit_counts())
