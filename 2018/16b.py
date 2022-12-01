import file_loader

input_string = file_loader.get_input()



from typing import Tuple, List, Set

Register = Tuple[int, int, int, int]
Instruction = Tuple[int, int, int, int]


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


instructions_dict = {
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


def get_matches(before: Register, after: Register, a: int, b: int, c: int) -> Set[str]:
    ret: Set[str] = set()
    for name, instruction in instructions_dict.items():
        e = instruction(before, a, b, c)
        if e == after:
            ret.add(name)
    return ret


groupings = input_string.split("\n\n\n")[0].split("\n\n")
opcode_to_instruction_candidates = {}
for grouping in groupings:
    lines = grouping.splitlines()
    before0, before1, before2, before3 = [int(x) for x in lines[0][9:-1].split(",", 3)]
    opcode, instruction_a, instruction_b, instruction_c = [int(x) for x in lines[1].split(maxsplit=3)]
    after0, after1, after2, after3 = [int(x) for x in lines[2][9:-1].split(",", 3)]
    matches = get_matches(
        (before0, before1, before2, before3),
        (after0, after1, after2, after3),
        instruction_a, instruction_b, instruction_c
    )
    if opcode not in opcode_to_instruction_candidates:
        opcode_to_instruction_candidates[opcode] = matches
    else:
        opcode_to_instruction_candidates[opcode] = opcode_to_instruction_candidates[opcode].intersection(matches)

opcode_to_instructions = {}
while len(opcode_to_instruction_candidates) > 0:
    instruction_to_remove = None
    for opcode, instructions in opcode_to_instruction_candidates.items():
        if len(instructions) == 1:
            instruction_to_remove = instructions.pop()
            opcode_to_instructions[opcode] = instruction_to_remove
            break
    opcodes_to_remove = set()
    for opcode, instructions in opcode_to_instruction_candidates.items():
        if instruction_to_remove in instructions:
            instructions.remove(instruction_to_remove)
        if len(instructions) == 0:
            opcodes_to_remove.add(opcode)
    for opcode in opcodes_to_remove:
        opcode_to_instruction_candidates.pop(opcode, None)


program = input_string.split("\n\n\n\n")[1].splitlines()
register: Register = (0, 0, 0, 0)
for line in program:
    opcode, a, b, c = line.split()
    instruction = instructions_dict[opcode_to_instructions[int(opcode)]]
    register = instruction(register, int(a), int(b), int(c))

print(register[0])