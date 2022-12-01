import re

import file_loader

input_string = file_loader.get_input()

min_x, max_x, min_y, max_y = [int(a) for a in
    re.search(r"^target area: x=([-]?\d+)\.\.([-]?\d+), y=([-]?\d+)\.\.([-]?\d+)", input_string).groups()
]

"""
To get maximum height, we need to max out our initial y speed whilst still hitting the target box
Our initial position is 0,0
Say our initial velocity is vx, vy
Observation: after 2*vy + 1 steps, the y-axis position of the probe will always be 0
Therefore, at 2*vy + 2 steps, the y coordinate of the probe is -1*vy - 1
Thus the maximum vy that still lands inside the target box is such that -1*vy - 1 = bottom of the target
"""

vy = -1*min_y - 1

"""
maximum height achieved when given initial y velocity of vy is vy(vy+1)/2
"""

print(int((vy*(vy+1)) / 2))
