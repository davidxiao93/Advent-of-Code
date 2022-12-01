import file_loader

input_string = file_loader.get_input()

grid = []
for line in input_string.splitlines():
    grid.append(list(line))

def get_num_neighbours_of(x, y, grid, t):
    count = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if x + dx < 0 or x + dx >= len(grid[0]):
                continue
            if y + dy < 0 or y + dy >= len(grid):
                continue
            if grid[y + dy][x + dx] == t:
                count += 1
    return count

def advance(grid):
    changes = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == ".":
                # open
                trees = get_num_neighbours_of(x, y, grid, "|")
                if trees >= 3:
                    changes.add((x, y, "|"))
            if c == "|":
                # tree
                lumbers = get_num_neighbours_of(x, y, grid, "#")
                if lumbers >= 3:
                    changes.add((x, y, "#"))
            if c == "#":
                # lumber
                lumbers = get_num_neighbours_of(x, y, grid, "#")
                trees = get_num_neighbours_of(x, y, grid, "|")
                if lumbers == 0 or trees == 0:
                    changes.add((x, y, "."))
    for x, y, n in changes:
        grid[y][x] = n


def score_grid(grid):
    trees = 0
    lumber = 0
    for row in grid:
        trees += row.count("|")
        lumber += row.count("#")
    return trees * lumber

def build_grid_state(grid):
    return "".join(["".join(row) for row in grid])


seen_states = {
    build_grid_state(grid): 0
}

target = 1000000000
t = 0
loop_size = 0
while t < target:
    advance(grid)
    new_state = build_grid_state(grid)
    if new_state in seen_states and loop_size == 0:
        loop_size = t - seen_states[new_state]
        t += (((target - t) // loop_size) - 1) * loop_size
    seen_states[new_state] = t
    t += 1

print(score_grid(grid))
