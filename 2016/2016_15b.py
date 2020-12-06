input = """Disc #1 has 17 positions; at time=0, it is at position 1.
Disc #2 has 7 positions; at time=0, it is at position 0.
Disc #3 has 19 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 0.
Disc #5 has 3 positions; at time=0, it is at position 0.
Disc #6 has 13 positions; at time=0, it is at position 5."""

# part 2
input += """\nDisc #7 has 11 positions; at time=0, it is at position 0."""

# input = """Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1."""

# valid positions for disc = -1 * initial_position % disc_positions + k disc_positions - disk number
# can use chinese remainder theorem

n = []
a = []

for line in input.splitlines():
    words = line.split()
    positions = int(words[3])
    offset = (-1 * int(words[-1][:-1]) - int(words[1][1:])) % positions
    n.append(positions)
    a.append(offset)



# Yoinked from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print(chinese_remainder(n, a))