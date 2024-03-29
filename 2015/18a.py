import file_loader

input_string = file_loader.get_input()
target = 100

class Light:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.next_state = None

    def calculate_next_state(self, grid):
        on_around = 0
        for dy in range(-1, 2):
            if self.y + dy < 0:
                continue
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if self.x + dx < 0:
                    continue
                try:
                    on_around += grid[self.y + dy][self.x + dx].state
                except IndexError:
                    pass
        if self.state == 1:
            self.next_state = 1 if on_around == 2 or on_around == 3 else 0
        else:
            self.next_state = 1 if on_around == 3 else 0

    def apply_next_state(self):
        if self.next_state is None:
            print("Invalid next state")
            exit(1)

        self.state = self.next_state
        self.next_state = None


grid = []
for y, line in enumerate(input_string.splitlines()):

    grid.append([
        Light(x, y, 1 if l == "#" else 0)
        for x, l in enumerate(line)
    ])

def update_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x].calculate_next_state(grid)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x].apply_next_state()

def pretty_print_grid(grid):
    for row in grid:
        print("".join([
            "#" if l.state else "." for l in row
        ]))

for i in range(target):
    update_grid(grid)

# pretty_print_grid(grid)
print(sum([l.state for row in grid for l in row]))
