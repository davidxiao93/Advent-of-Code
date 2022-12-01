import file_loader

input_string = file_loader.get_input()


values = [0] + sorted([int(x) for x in input_string.splitlines()])

diffs = {
    1: 0,
    2: 0,
    3: 1 # this comes from the last adapter -> device
}

for a, b in zip(values, values[1:]):
    diffs[b - a] += 1

print(diffs[1] * diffs[3])




