input = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

target = int(sum(input) / 4)

import itertools

size = 1
candidates = []
while len(candidates) == 0:
    size += 1
    candidates = [list(x) for x in itertools.combinations(input, size) if sum(x) == target]

def list_product(l):
    product = 1
    for x in l:
        product *= x
    return product

entanglements = [list_product(x) for x in candidates]
entanglements.sort()
print(entanglements[0])

