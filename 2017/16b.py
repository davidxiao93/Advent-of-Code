import file_loader

input_string = file_loader.get_input()
starting_pos = "abcdefghijklmnop"

# input_string = """s1,x3/4,pe/b"""
# starting_pos = "abcde"


def spin(s, x):
    return s[-1 * x:] + s[: -1 * x]

def exchange(s, a, b):
    l = list(s)
    t = l[a]
    l[a] = l[b]
    l[b] = t
    return "".join(l)

def partner(s, a, b):
    ai = s.index(a)
    bi = s.index(b)
    return exchange(s, ai, bi)

def dance(instructions, s):
    for instruction in instructions:
        if instruction.startswith('s'):
            s = spin(s, int(instruction[1:]))
        elif instruction.startswith('x'):
            sp = instruction.split('/')
            a = int(sp[0][1:])
            b = int(sp[1])
            s = exchange(s, a, b)
        elif instruction.startswith('p'):
            sp = instruction.split('/')
            a = sp[0][1:]
            b = sp[1]
            s = partner(s, a, b)
        else:
            print("wtf")
            exit(1)
    return s


s = starting_pos
instructions = input_string.split(",")

dance_map = {}

### hunt for a loop
i = 0
loop_size = None
loop_offset = None
while i < 1000000000:
    if s not in dance_map:
        dance_map[s] = i
        s = dance(instructions, s)
        i += 1
    else:
        loop_size = i - dance_map[s]
        loop_offset = dance_map[s]
        break

### Simplify
target = 1000000000
target -= loop_offset
target = target % loop_size

### find target in dance_map
for key, value in dance_map.items():
    if value == target:
        print(key)
        break

