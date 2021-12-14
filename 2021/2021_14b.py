from typing import Dict

input = """KBKPHKHHNBCVCHPSPNHF

OP -> H
CF -> C
BB -> V
KH -> O
CV -> S
FV -> O
FS -> K
KO -> C
PP -> S
SH -> K
FH -> O
NF -> H
PN -> P
BO -> H
OK -> K
PO -> P
SF -> K
BF -> P
HH -> S
KP -> H
HB -> N
NP -> V
KK -> P
PF -> P
BK -> V
OF -> H
FO -> S
VC -> P
FK -> B
NK -> S
CB -> B
PV -> C
CO -> N
BN -> C
HV -> H
OC -> N
NB -> O
CS -> S
HK -> C
VS -> F
BH -> C
PC -> S
KC -> O
VO -> P
FB -> K
BV -> V
VN -> N
ON -> F
VH -> H
CN -> O
HO -> O
SV -> O
SS -> H
KF -> N
SP -> C
NS -> V
SO -> F
BC -> P
HC -> C
FP -> H
OH -> S
OB -> S
HF -> V
SC -> B
SN -> N
VK -> C
NC -> V
VV -> S
SK -> K
PK -> K
PS -> N
KB -> S
KS -> C
NN -> C
OO -> C
BS -> B
NV -> H
FF -> P
FC -> N
OS -> H
KN -> N
VP -> B
PH -> N
NH -> S
OV -> O
FN -> V
CP -> B
NO -> V
CK -> C
VF -> B
HS -> B
KV -> K
VB -> H
SB -> S
BP -> S
CC -> F
HP -> B
PB -> P
HN -> P
CH -> O"""

polymer = input.splitlines()[0]
rules_lines = input.splitlines()[2:]
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

