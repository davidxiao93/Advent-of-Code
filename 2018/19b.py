input = """#ip 2
addi 2 16 2
seti 1 4 3
seti 1 5 1
mulr 3 1 5
eqrr 5 4 5
addr 5 2 2
addi 2 1 2
addr 3 0 0
addi 1 1 1
gtrr 1 4 5
addr 2 5 2
seti 2 9 2
addi 3 1 3
gtrr 3 4 5
addr 5 2 2
seti 1 6 2
mulr 2 2 2
addi 4 2 4
mulr 4 4 4
mulr 2 4 4
muli 4 11 4
addi 5 7 5
mulr 5 2 5
addi 5 4 5
addr 4 5 4
addr 2 0 2
seti 0 1 2
setr 2 1 5
mulr 5 2 5
addr 2 5 5
mulr 2 5 5
muli 5 14 5
mulr 5 2 5
addr 4 5 4
seti 0 6 0
seti 0 6 2"""

# input = """#ip 0
# seti 5 0 1
# seti 6 0 2
# addi 0 1 0
# addr 1 2 3
# setr 1 0 0
# seti 8 0 4
# seti 9 0 5"""

from typing import Tuple, List
Register = Tuple[int, int, int, int, int, int]


def addr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] + r[b]
    return tuple(r)

def addi(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] + b
    return tuple(r)

def mulr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] * r[b]
    return tuple(r)

def muli(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] * b
    return tuple(r)

def banr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] & r[b]
    return tuple(r)

def bani(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] & b
    return tuple(r)

def borr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] | r[b]
    return tuple(r)

def bori(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a] | b
    return tuple(r)

def setr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = r[a]
    return tuple(r)

def seti(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = a
    return tuple(r)

def gtir(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if a > r[b] else 0
    return tuple(r)

def gtri(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] > b else 0
    return tuple(r)

def gtrr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] > r[b] else 0
    return tuple(r)

def eqir(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if a == r[b] else 0
    return tuple(r)

def eqri(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] == b else 0
    return tuple(r)

def eqrr(before: Register, a: int, b: int, c: int) -> Register:
    r = list(before)
    r[c] = 1 if r[a] == r[b] else 0
    return tuple(r)


instructions = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}


register: Register = (1, 0, 0, 0, 0, 0)
instruction_register = int(input.splitlines()[0].split()[1])
program = input.splitlines()[1:]


"""
    00 addi 2 16 2      --- next is 17
    01 seti 1 4 3       --- r[3] = 1
    02 seti 1 5 1       --- r[5] = 1
    03 mulr 3 1 5       --- r[5] = r[1] * r[3]
    04 eqrr 5 4 5       --- r[5] = 1 if r[5] == r[4] else 0
    05 addr 5 2 2       === jump by value in register[5] (0 or 1), determined by instruction 04
                            if r[5] == r[4], next is 7 else, next is 6                            
    06 addi 2 1 2       === next is 08
    07 addr 3 0 0       --- r[0] += r[3]
                            only executed if r[5] == r[4]
    08 addi 1 1 1       --- r[1] += 1
    09 gtrr 1 4 5       --- r[5] = 1 if r[1] > r[4] else 0
    10 addr 2 5 2       === jump by value in register[5] (0 or 1), determined by instruction 09
    11 seti 2 9 2       === next is 03
    12 addi 3 1 3       --- r[3] += 1
    13 gtrr 3 4 5       --- r[5] = 1 if r[3] > r[4] else 0
    14 addr 5 2 2       === jump by value in register[5] (0 or 1), deterined by instruction 13
    15 seti 1 6 2       === next is 02
    16 mulr 2 2 2       === exit
Everything below this line is all setup code. It is never executed a second time
    17 addi 4 2 4       --- r[4] += 2
    18 mulr 4 4 4       --- r[4] *= r[4]
    19 mulr 2 4 4       --- r[4] *= r[2]
    20 muli 4 11 4      --- r[4] *= 11
    21 addi 5 7 5       --- r[5] += 7
    22 mulr 5 2 5       --- r[5] *= r[2]
    23 addi 5 4 5       --- r[5] += 4
    24 addr 4 5 4       --- r[4] += r[5]
    25 addr 2 0 2       === jump by value in register[0]
    26 seti 0 1 2       === next is 01
    27 setr 2 1 5       --- r[5] = r[2]
    28 mulr 5 2 5       --- r[5] *= r[2]
    29 addr 2 5 5       --- r[5] += r[2]
    30 mulr 2 5 5       --- r[5] *= r[2]
    31 muli 5 14 5      --- r[5] *= 14
    32 mulr 5 2 5       --- r[5] *= r[2]
    33 addr 4 5 4       --- r[4] += r[5]
    34 seti 0 6 0       --- r[0] = 0
    35 seti 0 6 2       === next is 01
"""


"""
The purpose of the code can be explained by understanding what is happening
- r[1] is iterated from 1 to r[4] (inclusive)
     there is a check to see if r[1] * r[3] == r[4]
     if successful, then r[0] is incremented by r[3]
next r[3] is incremented. r[3] is incremented from 1 to r[4] (inclusive)
in other words, r[0] is only incremented by r[3] when r[3] is a factor of r[4]
and as r[3] is being incremented from 1 to r[4] (inclusive) r[0] is increased by every factor of r[4]

in short, the program halts when r[0] is equal to the summation of all factors of r[4] (when at instruction 1)

"""

while True:
    words = program[register[instruction_register]].split()
    # perform program
    if register[instruction_register] == 1:
        # We've got our value for r[4]
        break
    register = instructions[words[0]](register, int(words[1]), int(words[2]), int(words[3]))
    # check if incrementing causes halting
    if 0 <= register[instruction_register] + 1 < len(program):
        pass
    else:
        break
    # increment instruction register
    register = addi(register, instruction_register, 1, instruction_register)

import math
sum_factors = 0
for i in range(1, int(math.ceil(math.sqrt(register[4])))):
    if register[4] % i == 0:
        sum_factors += i
        sum_factors += int(register[4] // i)

print(sum_factors)