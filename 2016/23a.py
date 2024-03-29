import file_loader

input_string = file_loader.get_input()

# input_string = """cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a"""

registers = {
    'a': 7,
    'b': 0,
    'c': 0,
    'd': 0
}

def evaluate_word(w: str):
    if w.isalpha():
        return registers[w]
    else:
        return int(w)

instructions = input_string.splitlines()
current_instruction = 0

while 0 <= current_instruction < len(instructions):
    words = instructions[current_instruction].split()
    if words[0] == "cpy":
        if not words[2].isalpha():
            pass
        else:
            registers[words[2]] = evaluate_word(words[1])
        current_instruction += 1
    elif words[0] == "inc":
        if not words[1].isalpha():
            pass
        else:
            registers[words[1]] += 1
        current_instruction += 1
    elif words[0] == "dec":
        if not words[1].isalpha():
            pass
        else:
            registers[words[1]] -= 1
        current_instruction += 1
    elif words[0] == "jnz":
        if evaluate_word(words[1]) == 0:
            current_instruction += 1
        else:
            if not words[2].isalpha():
                current_instruction += int(words[2])
            else:
                current_instruction += registers[words[2]]
    elif words[0] == "tgl":
        offset = evaluate_word(words[1])
        toggle_instruction_index = current_instruction + offset
        if 0 <= toggle_instruction_index < len(instructions):
            instruction = instructions[toggle_instruction_index]
            if "inc" in instruction:
                instruction = instruction.replace("inc", "dec")
            elif "dec" in instruction:
                instruction = instruction.replace("dec", "inc")
            elif "jnz" in instruction:
                instruction = instruction.replace("jnz", "cpy")
            elif "cpy" in instruction:
                instruction = instruction.replace("cpy", "jnz")
            elif "tgl" in instruction:
                instruction = instruction.replace("tgl", "inc")

            instructions[toggle_instruction_index] = instruction
        current_instruction += 1
    else:
        print("unknown instruction")
        exit(1)

print(registers['a'])

