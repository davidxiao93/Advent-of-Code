import file_loader

input_string = file_loader.get_input()

values = [int(x) for x in input_string.splitlines()]

target = int(sum(values) / 4)

import itertools

size = 1
candidates = []
while len(candidates) == 0:
    size += 1
    candidates = [list(x) for x in itertools.combinations(values, size) if sum(x) == target]

def list_product(l):
    product = 1
    for x in l:
        product *= x
    return product

entanglements = [list_product(x) for x in candidates]
entanglements.sort()
print(entanglements[0])

