import file_loader

input_string = file_loader.get_input()


map = []

for line in input_string.splitlines():
    row = [ 0 if c == "." else 1
            for c in line ]

    map.append(row)

pos_x = 0
pos_y = 0

delta_x = 3
delta_y = 1

tree_count = 0

while pos_y < len(map):

    tree_count += map[pos_y][pos_x]

    pos_x += delta_x
    pos_x = pos_x % len(map[0])
    pos_y += delta_y

print(tree_count)