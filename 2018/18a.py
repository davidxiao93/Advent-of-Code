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

for i in range(10):
    advance(grid)

# for row in grid:
#     print("".join(row))


print(score_grid(grid))


