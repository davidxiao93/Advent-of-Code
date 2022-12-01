import file_loader

input_string = file_loader.get_input()

count = 0
for line in input_string.splitlines():
    sides = sorted([int(x) for x in line.split()])
    if sides[0] + sides[1] > sides[2]:
        count += 1

print(str(count))
