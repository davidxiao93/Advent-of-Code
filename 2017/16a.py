import file_loader

input_string = file_loader.get_input()
starting_pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

# input_string = """s1,x3/4,pe/b"""
# starting_pos = ['a', 'b', 'c', 'd', 'e']


def spin(s, x):
    return s[-1 * x:] + s[: -1 * x]

def exchange(s, a, b):
    t = s[a]
    s[a] = s[b]
    s[b] = t
    return s

def partner(s, a, b):
    ai = s.index(a)
    bi = s.index(b)
    return exchange(s, ai, bi)

s = starting_pos
for instruction in input_string.split(","):
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

print("".join(s))