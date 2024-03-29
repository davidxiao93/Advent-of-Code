from typing import Dict

import file_loader

input_string = file_loader.get_input()

polymer = input_string.splitlines()[0]
rules_lines = input_string.splitlines()[2:]
rules = {
    l.split("->")[0].strip(): [
        l.split("->")[0].strip()[0] + l.split("->")[1].strip(),
        l.split("->")[1].strip() + l.split("->")[0].strip()[1]
    ]
    for l in rules_lines
}

polymer_pairs = dict()
for a, b in zip(polymer, polymer[1:]):
    if a+b not in polymer_pairs:
        polymer_pairs[a+b] = 0
    polymer_pairs[a+b] += 1

def step(pairs: Dict[str, int]):
    new_pairs = dict()
    for p, c in pairs.items():
        pairs_to_add = []
        if p in rules:
            pairs_to_add += rules[p]
        else:
            pairs_to_add += [p]
        for pta in pairs_to_add:
            if pta not in new_pairs:
                new_pairs[pta] = 0
            new_pairs[pta] += c
    return new_pairs

for i in range(40):
    polymer_pairs = step(polymer_pairs)

# need to double count the first and last char
extra_pair = polymer[0] + polymer[-1]
if extra_pair not in polymer_pairs:
    polymer_pairs[extra_pair] = 0
polymer_pairs[extra_pair] += 1

# start counting - counts will be doubled!
counts = dict()
for p, c in polymer_pairs.items():
    for i in p:
        if i not in counts:
            counts[i] = 0
        counts[i] += c

# halving counts
for c, i in counts.items():
    counts[c] = int(i / 2)

print(max(counts.values()) - min(counts.values()))

