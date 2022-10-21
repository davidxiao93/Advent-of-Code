input = sorted([11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3])
target = 150


# input = sorted([20,15,10,5,5])
# target = 25

# input = sorted([3,4,3,5,5])
# target = 10

# input = [5, 5, 5]
# target = 10

"""
Note from future David:
The idea behind this was to somehow mark each container slightly differently. I used a small fraction
for each distinct container. That's what the deduplicate_input method is

In hindsight, recursion would have been a much better idea
"""

def deduplicate_input(l):
    mapping = {}
    new_l = []
    factor = 100
    for i in l:
        if i not in mapping:
            mapping[i] = 0
        new_l.append(i + mapping[i] / factor )

        mapping[i] += 1
    return new_l

l = deduplicate_input(input)

import math

def deduplicate_list_list(ll):
    output = []
    for l in ll:
        s = sorted(l)
        if s not in output:
            output.append(s)
    return output

def build_mapping():
    mapping = {}

    for t in range(target + 1):
        if t not in mapping:
            mapping[t] = []
        for c in l:
            # print("container", c)
            floor_c = math.floor(c)
            if t < floor_c:
                continue
            elif t == floor_c:
                mapping[t].append([c])
            else:
                for p in mapping[t - floor_c]:
                    if c in p:
                        continue
                    mapping[t].append([c] + p)
        mapping[t] = deduplicate_list_list(mapping[t])
    return mapping

result = build_mapping()[target]



print(len(deduplicate_list_list(result)))





