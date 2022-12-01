import re

import file_loader

input_string = file_loader.get_input()
# input_string = """target area: x=20..30, y=-10..-5"""
min_x, max_x, min_y, max_y = [int(a) for a in
    re.search(r"^target area: x=([-]?\d+)\.\.([-]?\d+), y=([-]?\d+)\.\.([-]?\d+)", input_string).groups()
]

x_steps_taken = dict()
y_steps_taken = dict()

for vy in range(min_y - 1, -1*min_y + 1):
    steps = 0
    current_y = 0
    vel_y = vy
    while current_y > (min_y - 1):
        steps += 1
        current_y += vel_y
        if min_y <= current_y <= max_y:
            if steps not in y_steps_taken:
                y_steps_taken[steps] = []
            y_steps_taken[steps].append(vy)
        vel_y -= 1

for vx in range(1, max_x + 1):
    steps = 0
    current_x = 0
    vel_x = vx
    while current_x <= max_x and steps < max(y_steps_taken.keys()):
        steps += 1
        current_x += vel_x
        if steps in y_steps_taken and min_x <= current_x <= max_x:
            if steps not in x_steps_taken:
                x_steps_taken[steps] = []
            x_steps_taken[steps].append(vx)

        if vel_x > 0:
            vel_x -= 1


count = set()
for k, v in x_steps_taken.items():
    # Have to use set as there can be (x,y) solutions that reach
    # the target box in multiple number of steps
    count = count.union({(x, y) for x in v for y in y_steps_taken[k]})

print(len(count))


