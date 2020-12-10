input = """set b 81
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""


"""
    00 set b 81
    01 set c b
    02 jnz a 2
    03 jnz 1 5
02
    04 mul b 100
    05 sub b -100000
    06 set c b
    07 sub c -17000
03, 31
    08 set f 1
    09 set d 2

23
    10 set e 2

19
    11 set g d
    12 mul g e
    13 sub g b
    14 jnz g 2
    15 set f 0
14
    16 sub e -1
    17 set g e
    18 sub g b
    19 jnz g -8
    # 11 - 19 ->
        after step 19:
        - if d > 1 and b is a multiple of d, then f = 0
        - e = b

    20 sub d -1
    21 set g d
    22 sub g b
    23 jnz g -13
    # 11 - 23
        - d = b
        - e = b
        - f = 1 if b is prime, 0 otherwise
        - g = 0

    24 jnz f 2
    25 sub h -1
24
    26 set g b
    27 sub g c
    28 jnz g 2
    29 jnz 1 3
28
    30 sub b -17
    31 jnz 1 -23

    # at instruction 28:
    - repeat
        - b += 17
        - d = b
        - e = b
        - g = b - c
        - h += 1 if old_b is not prime
    - until
        - g = 0


    # 03 - 31
        - b += 17
        - d = old_b
        - e = old_b
        - f = 1 if old_b is prime, 0 otherwise
        - h += 1 if old_b is not prime
        -
29
"""


def is_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True




registers = {
    'a': 1, # coprocessor debug mode off
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'g': 0,
    'h': 0
}

def evaluate(w):
    if w.isalpha():
        return registers[w]
    return int(w)


instructions = input.splitlines()
current_instruction = 0
iterations = 0
while 0 <= current_instruction < len(instructions) and iterations < 8000:
    iterations += 1
    instruction = instructions[current_instruction]

    print(registers)
    print(current_instruction, instruction)

    if current_instruction == 28:
        registers['h'] += 1 if not is_prime(registers['b']) else 0
        registers['b'] += 17
        registers['d'] = registers['b']
        registers['e'] = registers['b']
        registers['g'] = registers['b'] - registers['c']
        if registers['g'] == 0:
            current_instruction += 1
        continue

    if current_instruction == 23:
        registers['d'] = registers['b']
        registers['e'] = registers['b']
        registers['f'] = 1 if is_prime(registers['b']) else 0
        registers['g'] = 0
        current_instruction = 24
        continue

    if current_instruction == 11:
        print(registers)
        print(current_instruction, instruction)
        registers['e'] = registers['b']
        if registers['d'] > 1 and registers['b'] % registers['d'] == 0:
            registers['f'] = 0
        current_instruction = 20
        continue

    words = instruction.split()
    if words[0] == "set":
        registers[words[1]] = evaluate(words[2])
        current_instruction += 1
    elif words[0] == "sub":
        registers[words[1]] -= evaluate(words[2])
        current_instruction += 1
    elif words[0] == "mul":
        registers[words[1]] *= evaluate(words[2])
        current_instruction += 1
    elif words[0] == "jnz":
        if evaluate(words[1]) != 0:
            current_instruction += evaluate(words[2])
        else:
            current_instruction += 1

print("fin")



