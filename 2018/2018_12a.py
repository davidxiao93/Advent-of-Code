input = """#...#...##..####..##.####.#...#...#.#.#.#......##....#....######.####.##..#..#..##.##..##....#######

.#### => .
...#. => .
.##.. => #
#.##. => .
#..## => .
##### => #
####. => #
.##.# => #
#.### => .
...## => #
.#.## => #
#..#. => #
#.#.. => #
.###. => #
##.## => #
##..# => .
.#... => #
###.# => .
..##. => .
..... => .
###.. => #
..#.# => .
.#..# => #
##... => #
#.... => .
##.#. => .
..#.. => #
....# => .
#...# => .
#.#.# => #
..### => .
.#.#. => #"""

# input = """initial state: #..#.#..##......###...###
#
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #"""

initial_state = input.splitlines()[0].split(":", 1)[-1].strip()
mapping_strings = input.splitlines()[2:]

pots = set()
for i, p in enumerate(initial_state):
    if p == "#":
        pots.add(i)

def get_pot_contents(pots, i):
    return i in pots

mappings = {}
for m in mapping_strings:
    left, right = m.split(" => ")
    left = tuple(True if c == "#" else False for c in left)
    right = True if right == "#" else False
    mappings[left] = right



def advance_pots(pots, mappings):
    new_pots = pots.copy()
    # making the assumption that ..... => # is not a rule
    i = min(pots) - 5
    while i <= max(pots) + 5:
        t = (
            get_pot_contents(pots, i - 2),
            get_pot_contents(pots, i - 1),
            get_pot_contents(pots, i),
            get_pot_contents(pots, i + 1),
            get_pot_contents(pots, i + 2)
        )
        if t in mappings and mappings[t]:
            new_pots.add(i)
        elif i in new_pots:
                new_pots.remove(i)

        i += 1
    return new_pots

def pretty_print_pots(pots):
    lower_bound = min(pots)
    print(" " * (-1 * min(pots)) + "0")
    row = []
    for i in range(lower_bound, max(pots) + 1):
        row.append(
            "#" if get_pot_contents(pots, i) else "."
        )
    print("." * (min(pots)) + "".join(row))

for i in range(20):
    # pretty_print_pots(pots)
    pots = advance_pots(pots, mappings)

# pretty_print_pots(pots)

print(sum(pots))