input = """#ip 4
seti 123 0 3
bani 3 456 3
eqri 3 72 3
addr 3 4 4
seti 0 0 4
seti 0 5 3
bori 3 65536 5
seti 5557974 2 3
bani 5 255 2
addr 3 2 3
bani 3 16777215 3
muli 3 65899 3
bani 3 16777215 3
gtir 256 5 2
addr 2 4 4
addi 4 1 4
seti 27 9 4
seti 0 0 2
addi 2 1 1
muli 1 256 1
gtrr 1 5 1
addr 1 4 4
addi 4 1 4
seti 25 4 4
addi 2 1 2
seti 17 6 4
setr 2 2 5
seti 7 1 4
eqrr 3 0 2
addr 2 4 4
seti 5 7 4"""

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


register: Register = (0, 0, 0, 0, 0, 0)
instruction_register = int(input.splitlines()[0].split()[1])
program = input.splitlines()[1:]



"""
00 seti 123 0 3         --- r[3] = 123
01 bani 3 456 3         --- r[3] = r[3] & 456
02 eqri 3 72 3          --- r[3] = 1 if r[3] == 72 else 0
03 addr 3 4 4           === r[4] += r[3]
04 seti 0 0 4           === r[4] = 0, next is 1
Above is executed once
05 seti 0 5 3           --- r[3] = 0
06 bori 3 65536 5       --- r[5] = r[3] | 65536
07 seti 5557974 2 3     --- r[3] = 5557974
08 bani 5 255 2         --- r[2] = r[5] & 255 
09 addr 3 2 3           --- r[3] += r[2]
10 bani 3 16777215 3    --- r[3] = r[3] & 16777215
11 muli 3 65899 3       --- r[3] *= 65899
12 bani 3 16777215 3    --- r[3] = r[3] & 16777215
13 gtir 256 5 2         --- r[2] = 1 if 256 > r[5] else 0
14 addr 2 4 4           === r[4] += r[2]
15 addi 4 1 4           === r[4] += 1, next is 17
16 seti 27 9 4          === r[4] = 27, next is 28 
17 seti 0 0 2           --- r[2] = 0
18 addi 2 1 1           --- r[1] = r[2] + 1
19 muli 1 256 1         --- r[1] *= 256
20 gtrr 1 5 1           --- r[1] = 1 if r[1] > r[5] else 0
21 addr 1 4 4           === r[4] += r[1]
22 addi 4 1 4           === r[4] += 1, next is 24
23 seti 25 4 4          === r[4] = 25, next is 24
24 addi 2 1 2           --- r[2] += 1
25 seti 17 6 4          === r[4] = 17, next is 18
26 setr 2 2 5           --- r[5] = r[2]
27 seti 7 1 4           === r[4] = 7, next is 8
28 eqrr 3 0 2           --- r[2] = 1 if r[3] == r[0] else 0
29 addr 2 4 4           === r[4] += r[2]
30 seti 5 7 4           === r[4] = 5, next is 6

"""

"""
After inspecting the code
- The program will halt when it reaches instruction 31
- It reaches instruction 31 if r[2] = 1 at instruction 29
- r[2] is 1 at instruction 29 if r[3] == r[0] at instruction 28
so value of r[0] to set to make program halt in fewest instruction is the value of r[3] at the first
time instruction 28 is executed
"""
while True:
    words = program[register[instruction_register]].split()
    if register[instruction_register] == 28:
        print(register[3])
        break
    # perform program
    register = instructions[words[0]](register, int(words[1]), int(words[2]), int(words[3]))
    # check if incrementing causes halting
    if 0 <= register[instruction_register] + 1 < len(program):
        pass
    else:
        break
    # increment instruction register
    register = addi(register, instruction_register, 1, instruction_register)
