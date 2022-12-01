import file_loader

input_string = file_loader.get_input()

def is_valid(sides):
    sides = sorted([int(x) for x in sides])
    return sides[0] + sides[1] > sides[2]


count = 0
triple_lines = []
for line in input_string.splitlines():
    if len(triple_lines) != 3:
        triple_lines.append(line)
    if len(triple_lines) == 3:
        line0 = triple_lines[0].split()
        line1 = triple_lines[1].split()
        line2 = triple_lines[2].split()
        for i in range(3):
            if is_valid([line0[i], line1[i], line2[i]]):
                count += 1
        triple_lines = []

print(str(count))
