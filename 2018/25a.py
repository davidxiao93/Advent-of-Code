import file_loader

input_string = file_loader.get_input()

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3] - b[3])

constellations = []
for line in input_string.splitlines():
    x, y, z, t = (int(a) for a in line.split(","))
    s = (x, y, z, t)
    matching_constellations = []
    for c in constellations:
        for star in c:
            if distance(star, s) <= 3:
                matching_constellations.append(c)
                break
    resulting_constellation = {s}
    for c in matching_constellations:
        constellations.remove(c)
        resulting_constellation |= c
    constellations.append(frozenset(resulting_constellation))

print(len(constellations))
