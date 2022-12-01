import file_loader

input_string = file_loader.get_input()
scrambled = "fbgdceah"

# scrambled = "baecdfgh"

# input_string = """swap position 4 with position 0
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
for line in reversed(input_string.splitlines()):
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

