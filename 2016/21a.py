import file_loader

input_string = file_loader.get_input()
password = "abcdefgh"

# input_string = """swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d"""
# password = "abcde"


def swap_positions(s, x, y):
    l = list(s)
    t = l[x]
    l[x] = l[y]
    l[y] = t
    return "".join(l)

def swap_letters(s, x, y):
    s = s.replace(x, ".")
    s = s.replace(y, x)
    s = s.replace(".", y)
    return s

def rotate_right(s, d):
    d = d % len(s)
    return s[-1*d:] + s[:-1*d]

def rotate_position(s, x):
    i = s.index(x)
    d = 1 + i
    if i >= 4:
        d += 1
    return rotate_right(s, d)

def reverse(s, x, y):
    r = "".join(reversed(s[x:y+1]))
    return s[:x] + r + s[y+1:]

def move(s, x, y):
    c = s[x]
    r = s[:x] + s[x+1:]
    return r[:y] + c + r[y:]


scrambled = password
for line in input_string.splitlines():
    words = line.split()
    if words[0] == "swap":
        if words[1] == "position":
            scrambled = swap_positions(scrambled, int(words[2]), int(words[5]))
        elif words[1] == "letter":
            scrambled = swap_letters(scrambled, words[2], words[5])
        else:
            print("unknown instruction")
            exit(1)
    elif words[0] == "rotate":
        if words[1] == "left":
            scrambled = rotate_right(scrambled, -1 * int(words[2]))
        elif words[1] == "right":
            scrambled = rotate_right(scrambled, int(words[2]))
        elif words[1] == "based":
            scrambled = rotate_position(scrambled, words[-1])
        else:
            print("unknown instruction")
            exit(1)
    elif words[0] == "reverse":
        scrambled = reverse(scrambled, int(words[2]), int(words[4]))
    elif words[0] == "move":
        scrambled = move(scrambled, int(words[2]), int(words[5]))
    else:
        print("unknown instruction")
        exit(1)

print(scrambled)

