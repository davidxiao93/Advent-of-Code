import file_loader

input_string = file_loader.get_input()


mapping = {}
nodes = set()

for line in input_string.split("\n"):
    words = line.split()
    a = words[0]
    gl = 1 if words[2] == "gain" else -1
    c = gl * int(words[3])
    b = words[-1][:-1]

    key = "".join(sorted([a[0], b[0]]))
    nodes.add(a[0])
    nodes.add(b[0])
    if key not in mapping:
        mapping[key] = 0
    mapping[key] += c

# adding myself

for n in nodes:
    mapping[n + "Z"] = 0
nodes.add("Z")


# resume computation

list_nodes = sorted(list(nodes))

import itertools
happiest = -2000000
for permutation in itertools.permutations(list_nodes):
    l = list(permutation) + [permutation[0]]
    current_happiness = 0
    for a, b in zip(l, l[1:]):
        key = "".join(sorted([a, b]))
        current_happiness += mapping[key]
    if current_happiness > happiest:
        happiest = current_happiness

print(happiest)























