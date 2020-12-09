input = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 464
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""

# input = """set a 1
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


instructions = input.splitlines()

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



