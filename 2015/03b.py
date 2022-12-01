import file_loader

input_string = file_loader.get_input()

santa_pos = (0, 0)
robot_pos = (0, 0)

map = {
    (0,0): 1
}

def move_pos(c, pos):
    if c == '<':
        pos = (pos[0] - 1, pos[1])
    if c == '>':
        pos = (pos[0] + 1, pos[1])
    if c == '^':
        pos = (pos[0], pos[1] + 1)
    if c == 'v':
        pos = (pos[0], pos[1] - 1)
    return pos

def update_map(pos):
    global map
    if pos not in map:
        map[pos] = 0
    map[pos] += 1



for i, c in enumerate(input_string):
    if i%2 == 0:
        santa_pos = move_pos(c, santa_pos)
        update_map(santa_pos)
    else:
        robot_pos = move_pos(c, robot_pos)
        update_map(robot_pos)



print(len(map))