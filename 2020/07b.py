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


colour_contains = {}

def get_count(colour):
    if colour not in colour_contains:
        sum = 0
        for c, q in contains_mapping[colour]:
            sum += q * get_count(c) + q
        colour_contains[colour] = sum
    return colour_contains[colour]


print(get_count("shiny gold"))


