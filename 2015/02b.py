import file_loader

input_string = file_loader.get_input()


def ribbon_needed(l, w, h):
    sides = sorted([l, w, h])
    return l * w * h + 2 * sides[0] + 2 * sides[1]


total = 0
for dim in input_string.split():
    l, w, h = dim.split('x')
    total += ribbon_needed(int(l), int(w), int(h))

print(total)
