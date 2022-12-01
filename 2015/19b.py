import file_loader

input_string = file_loader.get_input()

"""
Note from future David:
This took me way too long to realise that calculating the number of steps was what the question
wanted, but it didn't want the actual path.
"""

lines_split = input_string.splitlines()

target_molecule = lines_split[-1]

target_molecule = target_molecule.replace("Rn", "(")
target_molecule = target_molecule.replace("Ar", ")")
target_molecule = target_molecule.replace("Y", ",")
target_molecule = "".join(["X" if c.isupper() else c for c in target_molecule if not c.islower()])


def reduce(o, t, c):
    count = 0
    while t in o:
        o = o.replace(t, "X", 1)
        count += 1
    return o, c + count

count = 0
last_count = -1

while last_count != count:
    last_count = count
    target_molecule, count = reduce(target_molecule, "XX", count)
    target_molecule, count = reduce(target_molecule, "X(X,X,X)", count)
    target_molecule, count = reduce(target_molecule, "X(X,X)", count)
    target_molecule, count = reduce(target_molecule, "X(X)", count)


print(count)
