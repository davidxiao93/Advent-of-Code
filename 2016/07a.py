import file_loader

input_string = file_loader.get_input()

def has_abba(s):
    for a, b, c, d in zip(s, s[1:], s[2:], s[3:]):
        if a == d and c == b and a != b:
            return True
    return False

import re

def has_tls(s):
    split = re.split("\\[|\\]", s)
    return_val = False
    for i, s in enumerate(split):
        if i%2 == 1:
            if has_abba(s):
                return False
        else:
            return_val = return_val or has_abba(s)
    return return_val

count = 0
for line in input_string.splitlines():
    if has_tls(line):
        count += 1

print(count)