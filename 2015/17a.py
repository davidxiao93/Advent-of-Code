import file_loader

input_string = file_loader.get_input()

sorted_input_values = sorted([int(x) for x in input_string.split("\n")])
target = 150

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

l = deduplicate_input(sorted_input_values)

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





