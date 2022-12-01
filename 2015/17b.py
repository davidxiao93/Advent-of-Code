import file_loader

input_string = file_loader.get_input()

sorted_input_values = sorted([int(x) for x in input_string.split("\n")])
target = 150

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

min_quantity = min([len(l) for l in result])

combinations = [l for l in result if len(l) == min_quantity]

print(len(combinations))


# print(deduplicate_list_list(result))





