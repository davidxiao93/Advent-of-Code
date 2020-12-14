serial = 9005

grid_size = 300

def get_power_level(x, y, serial):
    # x, y should be 1 indexed (i.e between 1 and 300 inclusive)
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level

def get_3x3_sum(grid, x, y):
    sum = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            sum += grid[y + j][x + i]
    return sum

def find_largest_3x3(grid):
    largest_power = None
    largest_x = None
    largest_y = None
    for y in range(1, grid_size - 1):
        for x in range(1, grid_size - 1):
            s = get_3x3_sum(grid, x, y)
            if largest_power is None or s > largest_power:
                largest_power = s
                # Note: no need to reindex, as x, y is the center in when zero indexed
                # But the question is asking for the top left coordinates with one-index
                largest_x = x
                largest_y = y
    return largest_x, largest_y

grid = []
for y in range(grid_size):
    row = []
    for x in range(grid_size):
        row.append(get_power_level(x + 1, y + 1, serial))
    grid.append(row)


x, y = find_largest_3x3(grid)
print(str(x) + "," + str(y))
