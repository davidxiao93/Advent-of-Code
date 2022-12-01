import file_loader

input_string = file_loader.get_input()

map = []
for i in range(1000):
    map.append([0] * 1000)


def turn_off(x, y):
    map[y][x] -= 1
    if map[y][x] < 0:
        map[y][x] = 0


def turn_on(x, y):
    map[y][x] += 1


def toggle(x, y):
    map[y][x] += 2


def act(func, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            func(x, y)


for line in input_string.split("\n"):
    if line.startswith("turn off"):
        func = turn_off
        coord = line[len("turn off"):]
    elif line.startswith("turn on"):
        func = turn_on
        coord = line[len("turn on"):]
    elif line.startswith("toggle"):
        func = toggle
        coord = line[len("toggle"):]
    else:
        continue

    coord1, coord2 = coord.split("through")
    x1, y1 = [int(x.strip()) for x in coord1.strip().split(",")]
    x2, y2 = [int(x.strip()) for x in coord2.strip().split(",")]

    act(func, x1, y1, x2, y2)


count = 0
for column in map:
    count += sum(column)

print(count)