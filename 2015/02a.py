import file_loader

input_string = file_loader.get_input()


def area_needed(l, w, h):
    sides = sorted([l * w, w * h, h * l])
    return 3 * sides[0] + 2 * sides[1] + 2 * sides[2]


total = 0
for dim in input_string.split():
    l, w, h = dim.split('x')
    total += area_needed(int(l), int(w), int(h))

print(total)
