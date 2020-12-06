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

input = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO"""

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



best_path = None
seen_values = set()

def traverse(replacements_used, current_value):
    global best_path, seen_values
    print("checking", current_value)
    if len(current_value) > len(target_molecule):
        return
    if current_value == target_molecule:
        if best_path is None:
            best_path = replacements_used
        elif len(best_path) > len(replacements_used):
            best_path = replacements_used
        return
    for r in replacements:
        next = build_replacements(current_value, r[0], r[1])
        for n in next:
            if n not in seen_values:
                seen_values.add(n)
                traverse(replacements_used + [r], n)

traverse([], "e")
print(best_path)



