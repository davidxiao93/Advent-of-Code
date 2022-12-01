import file_loader

input_string = file_loader.get_input()

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

instructions = input_string.splitlines()
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

