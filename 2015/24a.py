input = """1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113"""

values = [int(x) for x in input.splitlines()]

target = int(sum(values) / 3)

# find smallest combination of inputs that total 520
# if multiple, choose the one with smallest product
# return product

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

