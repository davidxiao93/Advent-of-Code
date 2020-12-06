input = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"""


# C(P(Ca(F))F)Al
# C(P(N)F)Al


import re


# ThCaSiThCaSi(CaFYCaSi(FYF)F)
# ThCaSiThCaSi(CaFYSi(FYF)F)     CaSi => Si
# ThCaSiThCaSi(CaFYCaF)     Ca => Si(FYF)
# ThCaSiThCaSi(FYF)     F => CaF * 2
#
# - find inner most brackets
# - decide if it is "X", "XYX", or "XYXYX"
#     - if "X"
#         - break it down until it is a single element
#     - if "XYX"
#         - break either side down until each side is a single element
#     - if "XYXYX"
#         - break it down until it is 3 single elements and two Ys
#     - expand leftwards until you reach ( or ) or Y
#         - break it down until it is a single element
# - check if the resulting pattern can be broken down
#
#





# C(CaCaCaSi(BPTiMg)Si(Si(Mg)Si(CaF)TiTiBSiThFYCaF)CaCaSiThCaPBSiThSiThCaCaPTi(PBSiTh(F))CaCaSiThCaSiThSi(Mg)CaPTiBP(F)SiThCaSi(F)BCaSi(CaP(F)PMgYCaF)CaPTiTiTiBPBSiThCaPTiBPBSi(F)BPBSi(CaF)BP(Si(F)(Si(BF)CaF)CaCaCaSiThSiThCaCaPBPTiTi(F)CaPTiBSiAl)PBCaCaCaCaCaSi(Mg)CaSiThF)
# ThCaSiThCaSi(CaFYCaSi(FYF)F)
# CaSi(FYF)
# CaSi(BPMg)
# SiThP(F)
# CaSi(F)
# Ti(Si(FYF)CaSi(BF)CaSi(TiMg)SiThCaSiThCaF)
# P(F)
# Si(F)
# TiTiTiTiBCaCaSi(CaCaFYF)
# SiThCaPTiBPTiBCaSiThSi(Mg)
# CaF



# e -> XX
# X -> XX
# X -> X Rn X Ar | X Rn X Y X Ar | X Rn X Y X Y X Ar
# X is not Rn, Y, Ar

# input = """e => H
# e => O
# H => HO
# H => OH
# O => HH
#
# HOHOHO"""

lines_split = input.splitlines()

replacements_unparsed = lines_split[:-2]
target_molecule = lines_split[-1]
initial_molecule = "e"



special_replacements = []
ordinary_replacements = []
for r in replacements_unparsed:
    i = r.split()[0].strip()
    o = r.split()[-1].strip()
    if "Rn" in o and "Ar" in o:
        special_replacements.append((i, o))
    else:
        ordinary_replacements.append((i, o))



def build_replacements(s, input, output):
    outputs = []
    find = s.find(input)
    while find != -1:
        outputs.append(s[:find] + output + s[find+len(input):])
        find = s.find(input, find + 1)
    return outputs


def get_possible_replacements(s, replacements):
    combinations = set()
    for r in replacements:
        ns = build_replacements(s, r[0], r[1])
        for n in ns:
            if len(n) > len(target_molecule):
                continue
            combinations.add(n)
    return combinations


def get_possible_unreplacements(s, replacements):
    combinations = set()
    for r in replacements:
        ns = build_replacements(s, r[1], r[0])
        for n in ns:
            if len(n) > len(target_molecule):
                continue
            combinations.add(n)
    return combinations


def is_singleton_element(s):
    return sum(1 for c in s if c.isupper()) == 1


def contains_singleton_element(l):
    return 0 < len([s for s in l if is_singleton_element(s)])


def brute_break_down(original, replacements) -> (str, int):
    """
    break down the string using brute force
    :param original: starting point of string
    :param replacements: replacement tuples that can be used
    :return: tuple of (str, int).
                the string represents the broken down version
                the int represents how many steps were taken to get there
            or None if not possible
    """
    unreplacement_combinations = {
        0: {original}
    }
    current_steps = 0
    while not contains_singleton_element(unreplacement_combinations[current_steps]):
        if len(unreplacement_combinations[current_steps]) == 0:
            return None
        unreplacement_combinations[current_steps + 1] = set()
        for combo in unreplacement_combinations[current_steps]:
            unreplacement_combinations[current_steps + 1] = \
                unreplacement_combinations[current_steps + 1] \
                    | get_possible_unreplacements(combo, replacements)
        current_steps += 1
    singleton_element = [e for e in unreplacement_combinations[current_steps]
                         if is_singleton_element(e)][0]
    return (singleton_element, current_steps)


def greedy_break_down(original, replacements):
    """
    break down the string using greedy approach
    :param original: starting point of string
    :param replacements: replacement tuples that can be used
    :return: tuple of (str, int).
                the string represents the broken down version
                the int represents how many steps were taken to get there
            or None if not possible
    """
    replacements_made = 0
    changes_to_make = len(replacements)
    while changes_to_make:
        counter = 0
        for r in replacements:
            additional_count = 0

            indexes = [m.start() for m in re.finditer(r[1], original)]
            indexes = [i for i in indexes
                       if i - 2 < 0
                            or i - 1 < 0
                            or (original[i - 2] != "R" and original[i - 1] != "n")]
            if len(indexes) > 0:
                i = indexes[0]
                additional_count = 1
                replacements_made += 1
                original = original[:i] + r[0] + original[i + len(r[1]):]

            counter += additional_count

        changes_to_make = counter
    return (original, replacements_made)


def ordinary_break_down(original):
    count = 0
    ordinarys_to_process = re.split('Rn|Ar|Y', original)
    ordinarys_to_process.sort(key=lambda s: -1 * len(s))
    ordinarys_to_process = [o for o in ordinarys_to_process if not is_singleton_element(o)]

    ordinary_map = {}
    for o in ordinarys_to_process:
        ordinary_map[o] = brute_break_down(o, ordinary_replacements)

    for o in ordinarys_to_process:
        if ordinary_map[o] is not None:
            while o in original:
                count += ordinary_map[o][1]
                original = original.replace(o, ordinary_map[o][0], 1)

    return (original, count)




count = 0
target_molecule, c = ordinary_break_down(target_molecule)
count += c

print(target_molecule)
print(count)

target_molecule, c = greedy_break_down(target_molecule, special_replacements + ordinary_replacements)
count += c


print(target_molecule)
print(count)

