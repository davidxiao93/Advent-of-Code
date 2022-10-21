from typing import List, Callable

input = """deal with increment 65
deal into new stack
deal with increment 25
cut -6735
deal with increment 3
cut 8032
deal with increment 71
cut -4990
deal with increment 66
deal into new stack
cut -8040
deal into new stack
deal with increment 18
cut -8746
deal with increment 42
deal into new stack
deal with increment 17
cut -8840
deal with increment 55
cut -4613
deal with increment 10
cut -5301
deal into new stack
deal with increment 21
cut -5653
deal with increment 2
cut 5364
deal with increment 72
cut -3468
deal into new stack
cut -9661
deal with increment 63
cut 6794
deal with increment 43
cut 2935
deal with increment 66
cut -1700
deal with increment 6
cut 5642
deal with increment 64
deal into new stack
cut -5699
deal with increment 43
cut -9366
deal with increment 42
deal into new stack
cut 2364
deal with increment 13
cut 8080
deal with increment 2
deal into new stack
cut -9602
deal with increment 51
cut 3214
deal into new stack
cut -2995
deal with increment 57
cut -8169
deal into new stack
cut 362
deal with increment 41
cut -4547
deal with increment 56
cut -1815
deal into new stack
cut 1554
deal with increment 71
cut 2884
deal with increment 44
cut -2423
deal with increment 4
deal into new stack
deal with increment 20
cut -2242
deal with increment 48
cut -716
deal with increment 29
cut -6751
deal with increment 45
cut -9511
deal with increment 75
cut -440
deal with increment 35
cut 6861
deal with increment 52
cut -4702
deal into new stack
deal with increment 28
cut 305
deal with increment 16
cut 7094
deal into new stack
cut 5175
deal with increment 30
deal into new stack
deal with increment 61
cut 1831
deal into new stack
deal with increment 25
cut 4043"""
num_cards = 119315717514047
num_shuffles = 101741582076661
target = 2020


shuffles = []
for line in input.splitlines():
    if "stack" in line:
        shuffles.append((0,0))
    elif "cut" in line:
        shuffles.append((1, int(line.split()[1])))
    else:
        shuffles.append((2, int(line.split()[-1])))

pos = target
import time
start = time.time()
shuffles = shuffles[::-1]


"""
First simplifiy the shuffle so that I can better understand what is going on
"""

inverses = {}
# List of (Lists to multiply with) to sum with
operands: List[List[int]] = [[1]]
for s, v in shuffles:
    if s == 0:
        # reverse
        for o in operands:
            o.append(-1)
        operands.append([-1])
    elif s == 1:
        # cut
        operands.append([v])
    else:
        # deal with increment
        if v not in inverses:
            inverses[v] = pow(v, -1, num_cards)
        for o in operands:
            o.append(inverses[v])

sum_operands = []
for operand in operands:
    v = 1
    for o in operand:
        v = (v * o) % num_cards
    sum_operands.append(v)

mul_op = sum_operands[0]
sum_op = sum(sum_operands[1:])
"""
We have how completely simplified a single complete shuffle to
(new_pos * mul_op + sum_op) % num_cards = old_pos

We can reapply this equation as many times as needed, but theres a lot of times to be applied
We can bring them all together into this (using geometric series)

old_pos_num_shuffles_ago = (new_pos * (mul_op^num_shuffles) + sum_op * (mul_op^num_shuffles - 1) / (mul_op - 1)) % num_cards

equivalent to 

old_pos_num_shuffles_ago = (new_pos * (mul_op^num_shuffles) % num_cards) 
                            + 
                           (sum_op * (mul_op^num_shuffles - 1) / (mul_op - 1)) % num_cards

the division by (mul_op - 1) definitely going to not result in a fraction, as this is a geometric series
of a sequence of integers
And as this is in modular arithmetic, we can find the inverse of it

old_pos_num_shuffles_ago = (new_pos * (mul_op^num_shuffles)) % num_cards
                            + 
                           (sum_op * (mul_op^num_shuffles - 1) * pow(mul_op - 1, -1, mod=num_cards)) % num_cards

my attention now turns to mul_op^num_shuffles % num_cards
lets call it biggie
This is large, but we can use the binary powers to work it out much faster

"""

biggie = mul_op
binary_powers = {
}

for i in range(0, len("{0:b}".format(num_shuffles))):
    binary_powers[2**i] = biggie
    biggie = (biggie * biggie) % num_cards

target = num_shuffles
biggie = 1
for binary_power in sorted(binary_powers.keys(), reverse=True):
    if target >= binary_power:
        biggie = (biggie * binary_powers[binary_power]) % num_cards
        target -= binary_power
assert(target == 0)


"""
yay we have biggie now
old_pos_num_shuffles_ago = (new_pos * biggie) % num_cards
                            + 
                           (sum_op * (biggie - 1) * pow(mul_op - 1, -1, mod=num_cards)) % num_cards
"""

old_pos = (2020 * biggie + sum_op * (biggie - 1) * pow(mul_op - 1, -1, mod=num_cards)) % num_cards

print(old_pos)