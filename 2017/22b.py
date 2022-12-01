import file_loader

input_string = file_loader.get_input()

#
# input_str = """..#
# #..
# ..."""


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

current_position = Point(x=0, y=0)
current_direction = 0
directions = [up, right, down, left]

def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)


states = [".", "W", "#", "F"]
infected = {}
def get_infected_state(p):
    if p in infected:
        return infected[p]
    return 0

lines = input_string.splitlines()
initial_grid_size = int((len(lines[0]) - 1)/2)
for y, r in enumerate(lines):
    for x, c in enumerate(r):
        if c == '#':
            infected[Point(x=x-initial_grid_size, y=y-initial_grid_size)] = 2


def pretty_print(infected, current_position, current_direction):
    for y in range(-5, 6):
        r = []
        for x in range(-5, 6):
            if Point(x, y) in infected:
                a = states[infected[Point(x, y)]]
            else:
                a = "."
            if Point(x, y) == current_position:
                b = ["^", ">", "v", "<"][current_direction] + " "
            else:
                b = "  "
            r.append(a + b)
        print("".join(r))


infections_caused = 0
for i in range(10000000):
    # pretty_print(infected, current_position, current_direction)
    # print("----", i)
    s = get_infected_state(current_position)
    if s == 0: # clean
        current_direction = (current_direction - 1) % 4
    elif s == 1: # weakened
        pass
    elif s == 2: # infected
        current_direction = (current_direction + 1) % 4
    elif s == 3: # flagged
        current_direction = (current_direction + 2) % 4
    else:
        print("wtf")
        exit(1)
    infected[current_position] = (s + 1) % len(states)
    if infected[current_position] == 2:
        infections_caused += 1
    current_position = add_point(current_position, directions[current_direction])
    # input_string("Press Enter to continue...")

# pretty_print(infected, current_position, current_direction)

print(infections_caused)



