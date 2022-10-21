input = """rotate right 1 step
swap position 2 with position 4
rotate based on position of letter g
rotate left 4 steps
swap position 6 with position 0
swap letter h with letter a
swap letter d with letter c
reverse positions 2 through 4
swap position 2 with position 4
swap letter d with letter e
reverse positions 1 through 5
swap letter b with letter a
rotate right 0 steps
swap position 7 with position 3
move position 2 to position 1
reverse positions 2 through 5
reverse positions 4 through 7
reverse positions 2 through 7
swap letter e with letter c
swap position 1 with position 7
swap position 5 with position 7
move position 3 to position 6
swap position 7 with position 2
move position 0 to position 7
swap position 3 with position 7
reverse positions 3 through 6
move position 0 to position 5
swap letter h with letter c
reverse positions 2 through 3
swap position 2 with position 3
move position 4 to position 0
rotate based on position of letter g
rotate based on position of letter g
reverse positions 0 through 2
swap letter e with letter d
reverse positions 2 through 5
swap position 6 with position 0
swap letter a with letter g
swap position 2 with position 5
reverse positions 2 through 3
swap letter b with letter d
reverse positions 3 through 7
swap position 2 with position 5
swap letter d with letter b
reverse positions 0 through 3
swap letter e with letter g
rotate based on position of letter h
move position 4 to position 3
reverse positions 0 through 6
swap position 4 with position 1
swap position 6 with position 4
move position 7 to position 5
swap position 6 with position 4
reverse positions 5 through 6
move position 0 to position 6
swap position 5 with position 0
reverse positions 2 through 5
rotate right 0 steps
swap position 7 with position 0
swap position 0 with position 2
swap position 2 with position 5
swap letter h with letter c
rotate left 1 step
reverse positions 6 through 7
swap letter g with letter a
reverse positions 3 through 7
move position 2 to position 4
reverse positions 0 through 6
rotate based on position of letter g
swap position 0 with position 6
move position 2 to position 0
rotate left 3 steps
reverse positions 2 through 5
rotate based on position of letter a
reverse positions 1 through 4
move position 2 to position 3
rotate right 2 steps
rotate based on position of letter f
rotate based on position of letter f
swap letter g with letter a
rotate right 0 steps
swap letter f with letter h
swap letter f with letter b
swap letter d with letter e
swap position 0 with position 7
move position 3 to position 0
swap position 3 with position 0
rotate right 4 steps
rotate based on position of letter a
reverse positions 0 through 7
rotate left 6 steps
swap letter d with letter h
reverse positions 0 through 4
rotate based on position of letter f
move position 5 to position 3
move position 1 to position 3
move position 6 to position 0
swap letter f with letter c
rotate based on position of letter h
reverse positions 6 through 7"""
scrambled = "fbgdceah"

# scrambled = "baecdfgh"

# input = """swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d"""
# scrambled = "decab"


def undo_swap_positions(s, x, y):
    ss = set()
    for c in s:
        l = list(c)
        t = l[x]
        l[x] = l[y]
        l[y] = t
        ss.add("".join(l))
    return ss

def undo_swap_letters(s, x, y):
    ss = set()
    for c in s:
        c = c.replace(x, ".")
        c = c.replace(y, x)
        c = c.replace(".", y)
        ss.add(c)
    return ss

def undo_rotate_right(s, d):
    ss = set()
    for c in s:
        d = d % len(c)
        d = -1 * d
        ss.add(c[-1*d:] + c[:-1*d])
    return ss

def undo_rotate_position(s, x):
    ss = set()
    for c in s:
        possibile_original_indexes = set()
        for o in range(len(c)):
            new_i = o + 1 + o
            if o >= 4:
                new_i += 1
            if c[new_i % len(c)] == x:
                possibile_original_indexes.add(o)
        for o in possibile_original_indexes:
            for q in undo_rotate_right([c], c.find(x) - o):
                ss.add(q)
    return ss

def undo_reverse(s, x, y):
    ss = set()
    for c in s:
        r = "".join(reversed(c[x:y+1]))
        ss.add(c[:x] + r + c[y+1:])
    return ss

def undo_move(s, y, x):
    ss = set()
    for c in s:
        q = c[x]
        r = c[:x] + c[x+1:]
        ss.add(r[:y] + q + r[y:])
    return ss


password = {scrambled}
for line in reversed(input.splitlines()):
    words = line.split()
    if words[0] == "swap":
        if words[1] == "position":
            password = undo_swap_positions(password, int(words[2]), int(words[5]))
        elif words[1] == "letter":
            password = undo_swap_letters(password, words[2], words[5])
        else:
            print("unknown instruction")
            exit(1)
    elif words[0] == "rotate":
        if words[1] == "left":
            password = undo_rotate_right(password, -1 * int(words[2]))
        elif words[1] == "right":
            password = undo_rotate_right(password, int(words[2]))
        elif words[1] == "based":
            password = undo_rotate_position(password, words[-1])
        else:
            print("unknown instruction")
            exit(1)
    elif words[0] == "reverse":
        password = undo_reverse(password, int(words[2]), int(words[4]))
    elif words[0] == "move":
        password = undo_move(password, int(words[2]), int(words[5]))
    else:
        print("unknown instruction")
        exit(1)

print(next(iter(password)))

