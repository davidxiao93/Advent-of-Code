import file_loader

input_string = file_loader.get_input()

pos = (0, 0)

map = {
    (0,0): 1
}

for c in input_string:
    if c == '<':
        pos = (pos[0] - 1, pos[1])
    if c == '>':
        pos = (pos[0] + 1, pos[1])
    if c == '^':
        pos = (pos[0], pos[1] + 1)
    if c == 'v':
        pos = (pos[0], pos[1] - 1)

    if pos not in map:
        map[pos] = 0
    map[pos] += 1

print(len(map))