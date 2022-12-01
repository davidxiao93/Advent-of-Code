from typing import List

import file_loader

input_string = file_loader.get_input()

def shift_left(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

def reverse(s, n):
    r = s[:n]
    r = r[::-1]
    return r + s[n:]

def knot_hash(message: List[int], lengths: List[int], current_pos, skip_size):
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


def build_lengths():
    s = []
    for c in input_string:
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

lengths = build_lengths()
message = build_message()



current_pos = 0
skip_size = 0
for i in range(64):
    message, current_pos, skip_size = knot_hash(message, lengths, current_pos, skip_size)


from functools import reduce

dense = []
for i in range(16):
    x = reduce(lambda a, b: a ^ b, message[i*16: i*16 + 16])
    dense.append(x)

hash = "".join(['{:02x}'.format(d) for d in dense])

print(hash)

