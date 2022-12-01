import file_loader

input_string = file_loader.get_input()

lines_split = input_string.splitlines()

replacements_unparsed = lines_split[:-2]
initial_molecule = lines_split[-1]



replacements = []
for r in replacements_unparsed:
    i = r.split()[0].strip()
    o = r.split()[-1].strip()

    replacements.append((i, o))


def build_replacements(s, input_string, output):
    split = s.split(input_string)
    outputs = []
    for i in range(len(split) - 1):
        z = [input_string if j != i else output for j in range(len(split)-1)] + [""]
        outputs.append("".join([j for k in zip(split, z) for j in k]))
    return outputs


combinations = set()
for r in replacements:
    ns = build_replacements(initial_molecule, r[0], r[1])
    for n in ns:
        combinations.add(n)

print(len(combinations))