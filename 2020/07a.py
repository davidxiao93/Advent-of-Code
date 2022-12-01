import file_loader

input_string = file_loader.get_input()

contains_mapping = {}

for line in input_string.splitlines():
    container, contained = [x.strip() for x in line.split("bags contain", 1)]
    if container not in contains_mapping:
        contains_mapping[container] = set()
    for c in contained.split(","):
        cs = c.strip().split()
        if "no" in cs:
            continue
        q = int(cs[0])
        t = " ".join(cs[1:3])

        contains_mapping[container].add((t, q))



# Colours in values are bags that can contain key colour
contained_mapping = {}
for container, contained in contains_mapping.items():
    for c in contained:
        if c[0] not in contained_mapping:
            contained_mapping[c[0]] = set()
        contained_mapping[c[0]].add(container)

# print(contained_mapping)


bags = set()

paths_to_explore = {"shiny gold"}

while len(paths_to_explore) != 0:
    p = paths_to_explore.pop()
    bags.add(p)
    if p in contained_mapping:
        for c in contained_mapping[p]:
            paths_to_explore.add(c)

bags.remove("shiny gold")
print(len(bags))







