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

register: Register = (0, 0, 0, 0, 0, 0)
instruction_register = int(input.splitlines()[0].split()[1])
program = input.splitlines()[1:]
while True:
    words = program[register[instruction_register]].split()

    # perform program
    register = instructions[words[0]](register, int(words[1]), int(words[2]), int(words[3]))

    # check if incrementing causes halting
    if 0 <= register[instruction_register] + 1 < len(program):
        pass
    else:
        break

    # increment instruction register
    register = addi(register, instruction_register, 1, instruction_register)

print(register[0])