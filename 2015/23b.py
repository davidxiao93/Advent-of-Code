import file_loader

input_string = file_loader.get_input()

registers = {
    'a': 1,
    'b': 0
}

import re

def parse_offset(o):
    d = 1 if o[0] == '+' else -1
    x = int(o[1:])
    return d * x

def process(instructions, current_index):
    # returns next index
    instruction = instructions[current_index]

    i_split = re.split(", | ", instruction)
    if i_split[0] == 'hlf':
        r = i_split[1]
        registers[r] = registers[r] / 2
        return current_index + 1
    if i_split[0] == 'tpl':
        r = i_split[1]
        registers[r] = registers[r] * 3
        return current_index + 1
    if i_split[0] == 'inc':
        r = i_split[1]
        registers[r] = registers[r] + 1
        return current_index + 1
    if i_split[0] == 'jmp':
        return current_index + parse_offset(i_split[1])
    if i_split[0] == 'jie':
        r = i_split[1]
        if registers[r] % 2 == 0:
            return current_index + parse_offset(i_split[2])
        return current_index + 1
    if i_split[0] == 'jio':
        r = i_split[1]
        if registers[r] == 1:
            return current_index + parse_offset(i_split[2])
        return current_index + 1

    print("unknown instruction", instruction)
    exit(1)

instructions = input_string.splitlines()

current_index = 0

while current_index < len(instructions):
    current_index = process(instructions, current_index)

print(registers['b'])
