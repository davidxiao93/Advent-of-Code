import file_loader

input_string = file_loader.get_input()

map = []

for line in input_string.splitlines():
    row = [ 0 if c == "." else 1
            for c in line ]

    map.append(row)


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

result = 1
for slope in slopes:
    pos_x = 0
    pos_y = 0
    tree_count = 0

    while pos_y < len(map):

        tree_count += map[pos_y][pos_x]

        pos_x += slope[0]
        pos_x = pos_x % len(map[0])
        pos_y += slope[1]
    # print("slope", slope, "found", tree_count)
    result *= tree_count

print(result)