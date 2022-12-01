"""
rules
- one step involves moving in the elevator up or down exactly one floor
- you must have at least one item, but at most two
- if you are in a state where a microship is unpowered but another microchip on the same floor is powered, then game over
-

"""
import file_loader

input_string = file_loader.get_input()


""" 0
F4 .  .  .  .  .  .  .  .  .  .  .
F3 .  .  .  .  .  .  .  .  .  .  .
F2 .  .  PM .  pM .  .  .  .  .  . 
F1 E  PG .  pG .  TG TM RG RM CG CM
"""


"""
After a lot of tinkering with BFS and trying to see if I could brute force a solution, I realised
that the sheer number of possible moves grows too fast, and that there are a lot of moves that 
would need to be made

After much thinking, I decided to work out what would be the minimum number of moves, if we
completely ignored the microchips getting fried constraint.

This will give a lower bound on what the solution can be
"""

MICROCHIP = "microchip"
GENERATOR = "generator"
floors = []
num_floors = 0
for i, line in enumerate(input_string.splitlines()):
    num_floors += 1
    parts = line.split(" a ")
    for state in parts:
        if GENERATOR in state:
            floors.append(i)
        elif MICROCHIP in state:
            floors.append(i)


# print(floors)


# Basic premise is to assume that E starts at the top, and then count
# how many turns it would take if the elevator could take 0 or 1 items

count = 0

# Because the problem starts with the elevator on the bottom floor
# Then we need to compensate for it
count -= num_floors - 1
# As the elevator is at the bottom, it will be able to carry with it to
# the top as a freebie
floors.remove(0)

for f in floors:
    count += 2 * (num_floors - 1 - f)
print(count)




"""
At this point I decided to just try out this value in the input_string.

And it works

I have no idea why the constraint about microchips can be completely ignored.
"""



