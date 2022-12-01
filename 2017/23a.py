import file_loader

input_string = file_loader.get_input()

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

instructions = input_string.splitlines()
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

print(mul_invoked)


