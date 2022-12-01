import file_loader

input_string = file_loader.get_input()

# input_string = """0
# 3
# 0
# 1
# -3"""

current_instruction = 0
instructions = [int(x) for x in input_string.splitlines()]
steps = 0
while 0 <= current_instruction < len(instructions):
    offset = instructions[current_instruction]
    if offset >= 3:
        instructions[current_instruction] -= 1
    else:
        instructions[current_instruction] += 1
    current_instruction += offset
    steps += 1

print(steps)
