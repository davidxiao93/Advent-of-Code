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

registers = {
    'a': 0,
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

mul_invoked = 0

instructions = input.splitlines()
current_instruction = 0
while 0 <= current_instruction < len(instructions):
    instruction = instructions[current_instruction]
    words = instruction.split()
    if words[0] == "set":
        registers[words[1]] = evaluate(words[2])
        current_instruction += 1
    elif words[0] == "sub":
        registers[words[1]] -= evaluate(words[2])
        current_instruction += 1
    elif words[0] == "mul":
        mul_invoked += 1
        registers[words[1]] *= evaluate(words[2])
        current_instruction += 1
    elif words[0] == "jnz":
        if evaluate(words[1]) != 0:
            current_instruction += evaluate(words[2])
        else:
            current_instruction += 1

print("fin")

print(mul_invoked)


