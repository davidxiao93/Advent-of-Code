import file_loader

input_string = file_loader.get_input()


from copy import deepcopy


def char_to_state(c):
    if c == "#":
        return 2 # occupied
    if c == "L":
        return 1 # vacant
    return 0

def state_to_char(s):
    if s == 2:
        return "#"
    if s == 1:
        return "L"
    return "."

grid = []
for line in input_string.splitlines():
    grid.append([char_to_state(c) for c in line])


def find_seat(grid, x, y, dx, dy):
    x += dx
    y += dy
    ret = 0
    while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        ret = grid[y][x]
        if ret != 0:
            return ret
        x += dx
        y += dy
    return ret


def count_visible_occupied(grid, x, y):
    count = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            if i == 0 and j == 0:
                continue
            visible_seat = find_seat(grid, x, y, i, j)
            if visible_seat == 2: # is occupied
                count += 1
    return count

def step_grid(grid):
    seat_changed = False
    new_grid = deepcopy(grid)
    for y, row in enumerate(grid):
        for x, s in enumerate(row):
            if s == 0:
                continue # no need to check floor
            visible_occupied = count_visible_occupied(grid, x, y)
            if s == 1 and visible_occupied == 0:
                new_grid[y][x] = 2
                seat_changed = True
            if s == 2 and visible_occupied >= 5:
                new_grid[y][x] = 1
                seat_changed = True

    return new_grid, seat_changed


def pretty_print(grid):
    for row in grid:
        print("".join([state_to_char(s) for s in row]))

def total_occupied(grid):
    return sum([sum([1 if s == 2 else 0 for s in row]) for row in grid])


seat_changed = True
while seat_changed:
    grid, seat_changed = step_grid(grid)

# pretty_print(grid)
print(total_occupied(grid))
