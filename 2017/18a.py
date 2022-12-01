import file_loader

input_string = file_loader.get_input()

# input_string = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2"""


registers = {}
last_sound = None

def evaluate(w: str):
    if w.isalpha():
        if w not in registers:
            registers[w] = 0
        return registers[w]
    return int(w)

def get_register(w: str):
    if w not in registers:
        registers[w] = 0
    return registers[w]


instructions = input_string.splitlines()

current_instruction = 0
while 0 <= current_instruction < len(instructions):
    instruction = instructions[current_instruction]

    words = instruction.split()

    if words[0] == "snd":
        last_sound = evaluate(words[1])
        current_instruction += 1
    elif words[0] == "set":
        registers[words[1]] = evaluate(words[2])
        current_instruction += 1
    elif words[0] == "add":
        if words[1] not in registers:
            registers[words[1]] = 0
        registers[words[1]] += evaluate(words[2])
        current_instruction += 1
    elif words[0] == "mul":
        if words[1] not in registers:
            registers[words[1]] = 0
        registers[words[1]] *= evaluate(words[2])
        current_instruction += 1
    elif words[0] == "mod":
        if words[1] not in registers:
            registers[words[1]] = 0
        registers[words[1]] = registers[words[1]] % evaluate(words[2])
        current_instruction += 1
    elif words[0] == "rcv":
        print(last_sound)
        break
    elif words[0] == "jgz":
        if evaluate(words[1]) > 0:
            current_instruction += evaluate(words[2])
        else:
            current_instruction += 1



