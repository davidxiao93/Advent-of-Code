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
    l.split("->")[0].strip(): l.split("->")[1].strip()
    for l in rules_lines
}

def step(current_polymer):

    new_chars = []

    for a, b in zip(current_polymer, current_polymer[1:]):
        new_chars.append(rules.get(a+b, ""))

    next_polymer = "".join([a+b for a, b in zip(current_polymer, new_chars)]) + current_polymer[-1]

    return next_polymer

for i in range(10):
    polymer = step(polymer)

counts = dict()
for s in polymer:
    if s not in counts:
        counts[s] = 0
    counts[s] += 1

print(max(counts.values()) - min(counts.values()))


