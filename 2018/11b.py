import file_loader

input_string = file_loader.get_input()
serial = int(input_string)

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

def get_square_sum(grid, x, y, side):
    sum = 0
    for j in range(side):
        for i in range(side):
            sum += grid[y + j][x + i]
    return sum

def get_next_square_sum_x(grid, old_sum, x, y, side):
    # old sum is the sum of the square with size (side-1), with x and y in top left
    for a in range(side -1):
        old_sum += grid[y+a][x+side-1]
        old_sum += grid[y+side-1][x+a]
    old_sum += grid[y+side-1][x+side-1]
    return old_sum

def find_largest_for_x_y(grid, x, y):
    sum = grid[y][x]
    best_sum = sum
    best_side = 1
    side = 1
    while y + side + 1 < grid_size and x + side + 1 < grid_size:
        side += 1
        new_sum = get_next_square_sum_x(grid, sum, x, y, side)
        if new_sum > best_sum:
            best_sum = new_sum
            best_side = side
        sum = new_sum
    return best_sum, best_side

def find_largest(grid):
    largest_sum = None
    best_x = None
    best_y = None
    best_side = None
    for y in range(grid_size):
        for x in range(grid_size):
            sum, side = find_largest_for_x_y(grid, x, y)
            if largest_sum is None or sum > largest_sum:
                largest_sum = sum
                best_x = x + 1
                best_y = y + 1
                best_side = side
    return best_x, best_y, best_side


grid = []
for y in range(grid_size):
    row = []
    for x in range(grid_size):
        row.append(get_power_level(x + 1, y + 1, serial))
    grid.append(row)


print(",".join([str(i) for i in find_largest(grid)]))

