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
target = 50000000000
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
    i = min(pots) - 3
    while i <= max(pots) + 3:
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


def get_gappage(pots):
    s = sorted(list(pots))
    t = tuple()
    for a, b in zip(s, s[1:]):
        t += (b-a,)
    return t



past_states = {}
past_states[get_gappage(pots)] = (0, min(pots))


i = 0
while i < target:
    pots = advance_pots(pots, mappings)
    gappage = get_gappage(pots)
    if gappage in past_states:
        # loop found
        offset = min(pots) - past_states[gappage][1]
        loop_size = i - past_states[gappage][0]
        remaining_generations = target - i - 1
        remaining_loops = remaining_generations // loop_size
        new_pots = set()
        for p in pots:
            new_pots.add(p + remaining_loops * offset)
        pots = new_pots
        i += remaining_loops * loop_size + 1
        past_states = {}
    else:
        past_states[gappage] = (i, min(pots))
        i += 1

print(sum(pots))
