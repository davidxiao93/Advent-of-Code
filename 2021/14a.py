import file_loader

input_string = file_loader.get_input()

polymer = input_string.splitlines()[0]
rules_lines = input_string.splitlines()[2:]
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


