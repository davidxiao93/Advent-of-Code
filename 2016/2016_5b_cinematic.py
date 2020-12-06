import hashlib

input = "wtnhxymk"


def hash(key, n):
    return hashlib.md5((key + str(n)).encode('utf-8')).hexdigest()

import random

def print_password(password):
    r = list('%08x' % random.randrange(16 ** 8))
    for i, c in enumerate(password):
        if len(c) != 0:
            r[i] = c
    print("\r" + "".join(r), end="")

index = 0
password = [''] * 8
filled = 0
while filled != 8:
    h = hash(input, index)
    print_password(password)
    if h.startswith("00000"):
        if h[5].isnumeric() and 0 <= int(h[5]) <= 7 and len(password[int(h[5])]) == 0:
            password[int(h[5])] = h[6]
            filled += 1
    index += 1

print_password(password)