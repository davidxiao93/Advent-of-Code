from typing import List
from functools import reduce


input = "uugsqrei"

# input = "flqrgnkx"


def shift_left(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

def reverse(s, n):
    r = s[:n]
    r = r[::-1]
    return r + s[n:]

def build_lengths(input):
    s = []
    for c in input:
        s.append(ord(c))
    s.append(17)
    s.append(31)
    s.append(73)
    s.append(47)
    s.append(23)
    return s

def build_message():
    s = []
    for i in range(256):
        s.append(i)
    return s

def knot(message: List[int], lengths: List[int], current_pos = 0, skip_size = 0):
    original_pos = current_pos
    message = shift_left(message, current_pos)
    current_pos = 0
    for i in lengths:
        message = reverse(message, i)
        message = shift_left(message, i + skip_size)
        current_pos = ((current_pos - i) - skip_size) % len(message)
        skip_size += 1
    new_message = message[current_pos:] + message[:current_pos]
    return shift_left(new_message, len(message) - original_pos), (original_pos + len(message) - current_pos) % len(message), skip_size

def knot_hash_binary(input):
    lengths = build_lengths(input)
    message = build_message()

    current_pos = 0
    skip_size = 0
    for i in range(64):
        message, current_pos, skip_size = knot(message, lengths, current_pos, skip_size)

    dense = []
    for i in range(16):
        x = reduce(lambda a, b: a ^ b, message[i * 16: i * 16 + 16])
        dense.append(x)

    return "".join([format(d, 'b').zfill(8) for d in dense])


print(sum([
    knot_hash_binary(input + "-" + str(i)).count("1")
    for i in range(128)
]))