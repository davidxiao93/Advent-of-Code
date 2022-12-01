import file_loader

input_string = file_loader.get_input()

values = [int(c) for c in input_string]

from itertools import cycle

def do_round(vs):
    nvs = []
    base_battern = [0, 1, 0, -1]
    for i in range(1, len(vs) + 1):
        pattern = [base_battern[j//i] for j in range(len(base_battern) * i)][1:] + [0]
        nv = sum([
            a*b for a, b in zip(vs, cycle(pattern))
        ])
        nvs.append(abs(nv) % 10)
    return nvs

for i in range(100):
    values = do_round(values)

print("".join([str(x) for x in values[:8]]))
