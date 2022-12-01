import file_loader

input_string = file_loader.get_input()


#
# input_string = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""
#
# input_string = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""

values = [-3, 0] + sorted([int(x) for x in input_string.splitlines()])
values = values + [max(values)+3]

"""

Insight: Where there is a difference of 3, that must be kept
-> break the sequence down where there is a difference of 3
"""

all_groups = []
while len(values) != 0:
    counter = 1
    while counter + 1 < len(values) and values[counter + 1] - values[counter] != 3:
        counter += 1
    all_groups.append(values[:counter + 2])
    values = values[counter:]

# print(all_groups)

patterns = {}
for group in all_groups:
    # convert into diff pattern
    p = tuple()
    for a, b in zip(group, group[1:]):
        p += tuple([b - a])
    if len(p) != 0:
        if p not in patterns:
            patterns[p] = 0
        patterns[p] += 1

"""

patterns are like (3, 1, 1, 3)

"""
# print(patterns)


# mapping from number of 1-diffs to possibilities
ones = {
    0: 1,
    1: 1,
    2: 2
}

max_ones = 0
for p in patterns:
    if p.count(1) > max_ones:
        max_ones = p.count(1)

for i in range(max_ones + 1):
    if i not in ones:
        ones[i] = 2*ones[i - 1]
        if i - 4 in ones:
            ones[i] -= ones[i-4]

combo = 1
for p, quantity in patterns.items():
    combo *= ones[p.count(1)] ** quantity

print(combo)






