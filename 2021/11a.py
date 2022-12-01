import file_loader

input_string = file_loader.get_input()

energy_levels = dict()
max_y = len(input_string.splitlines())
max_x = len(input_string.splitlines()[0])

neighbours = {(x, y) for x in range(-1, 2) for y in range(-1, 2)} - {(0,0)}

for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        energy_levels[(x, y)] = int(c)

NUM_STEPS = 100
num_flashes = 0

for i in range(NUM_STEPS):
    to_flash = set()
    flashed = set()
    for y in range(max_y):
        for x in range(max_x):
            energy_levels[(x, y)] += 1
            if energy_levels[(x, y)] == 10 and (x, y) not in flashed:
                to_flash.add((x, y))
    while len(to_flash) > 0:
        next_to_flash = to_flash.pop()
        for n in neighbours:
            neighbour = (next_to_flash[0] + n[0], next_to_flash[1] + n[1])
            if neighbour not in energy_levels or neighbour in flashed or neighbour in to_flash:
                # outside grid, already flashed or will be flashed
                continue
            energy_levels[neighbour] += 1
            if energy_levels[neighbour] == 10:
                to_flash.add(neighbour)
        flashed.add(next_to_flash)

    for f in flashed:
        energy_levels[f] = 0

    num_flashes += len(flashed)

print(num_flashes)