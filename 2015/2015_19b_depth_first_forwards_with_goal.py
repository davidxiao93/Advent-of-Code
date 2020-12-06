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



replacements = []
for r in replacements_unparsed:
    i = r.split()[0].strip()
    o = r.split()[-1].strip()
    replacements.append((i, o))

replacements.sort(key=lambda r: -1 * (len(r[1]) - len(r[0])))


def build_replacements(s, input, output):
    outputs = []
    find = s.find(input)
    while find != -1:
        outputs.append(s[:find] + output + s[find+len(input):])
        find = s.find(input, find + 1)
    return outputs




import difflib
score_mapping = {}
def get_score(s):
    if s in score_mapping:
        return score_mapping[s]
    score = 0
    for g in difflib.ndiff(s, target_molecule):
        if g[0] == '+' or g[0] == '-':
            score -= 1
    score_mapping[s] = score
    return score


def traverse():
    values_to_check = [("e", 0)]
    seen_values = set()

    while len(values_to_check) > 0:

        # fancy sort to make the "best candidate" at the end
        # values_to_check.sort(
        #     key=lambda v: get_score(v[0])
        # )


        # continue with normal depth first search
        s, i = values_to_check[-1]

        print(len(values_to_check), i, s)
        values_to_check = values_to_check[:-1]

        if s == target_molecule:
            print(i)
            return

        if len(s) > len(target_molecule):
            continue

        if s in seen_values:
            continue
        seen_values.add(s)

        for r in replacements:
            new_nodes = build_replacements(s, r[0], r[1])
            for n in new_nodes:
                values_to_check.append((n, i + 1))



traverse()




