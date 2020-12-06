input = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 18 c
cpy 11 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0
}

instructions = input.splitlines()
current_instruction = 0

while current_instruction < len(instructions):
    words = instructions[current_instruction].split()
    if words[0] == "cpy":
        v = words[1]
        if v.isnumeric():
            registers[words[2]] = int(v)
        else:
            registers[words[2]] = registers[words[1]]
        current_instruction += 1
    elif words[0] == "inc":
        registers[words[1]] += 1
        current_instruction += 1
    elif words[0] == "dec":
        registers[words[1]] -= 1
        current_instruction += 1
    elif words[0] == "jnz":
        if words[1].isnumeric():
            is_zero = int(words[1]) == 0
        else:
            is_zero = registers[words[1]] == 0
        if is_zero:
            current_instruction += 1
        else:
            current_instruction += int(words[2])

print(registers['a'])

