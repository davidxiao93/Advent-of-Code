"""
rules
- one step involves moving in the elevator up or down exactly one floor
- you must have at least one item, but at most two
- if you are in a state where a microship is unpowered but another microchip on the same floor is powered, then game over
-

"""
input = """The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
The third floor contains nothing relevant.
The fourth floor contains nothing relevant."""


"""
After part a, I tried the same technique here.
"""


MICROCHIP = "microchip"
GENERATOR = "generator"
floors = []
num_floors = 0
for i, line in enumerate(input.splitlines()):
    num_floors += 1
    parts = line.split(" a ")
    for state in parts:
        if GENERATOR in state:
            floors.append(i)
        elif MICROCHIP in state:
            floors.append(i)

# Add in the extra elements
for i in range(4):
    floors.append(0)


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
Once again I decided to just try this value as it was a hard lower bound of what 
the real answer could be

And it works

Again, I have no idea why the constraint about microchips can be completely ignored.
"""



