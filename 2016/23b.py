input = """cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 87 c
jnz 97 d
inc a
inc d
jnz d -2
inc c
jnz c -5"""

registers = {
    'a': 12,
    'b': 0,
    'c': 0,
    'd': 0
}

"""
    00 cpy a b
    01 dec b
    02 cpy a d
    03 cpy 0 a
09
    04 cpy b c
07
    05 inc a
    06 dec c
    07 jnz c -2
    08 dec d
    09 jnz d -5
    # Steps 04 - 09 is:
        r = registers at step 04
        r[a] += r[b]*r[d]
        r[b] = r[b]
        r[c] = 0
        r[d] = 0

    10 dec b
    11 cpy b c
    12 cpy c d
15
    13 dec d
    14 inc c
    15 jnz d -2
    # Steps 13 - 15 is:
         r = registers at step 13
         r[a] = r[a]
         r[b] = r[b]
         r[c] = 2*r[c]
         r[d] = 0

    16 tgl c
    17 cpy -16 c
    18 jnz 1 c
    19 cpy 87 c
25
    20 jnz 97 d
23
    21 inc a
    22 inc d
    23 jnz d -2
    24 inc c
    25 jnz c -5
"""

def evaluate_word(w: str):
    if w.isalpha():
        return registers[w]
    else:
        return int(w)

instructions = input.splitlines()
current_instruction = 0

toggled_instructions = set()

while 0 <= current_instruction < len(instructions):
    words = instructions[current_instruction].split()
    shortcut = False
    if current_instruction == 4:
        can_take_shortcut = True
        for i in [4, 5, 6, 7, 8, 9]:
            if i in toggled_instructions:
                can_take_shortcut = False
        if can_take_shortcut:
            registers['a'] = registers['b'] * registers['d']
            registers['c'] = 0
            registers['d'] = 0
            current_instruction = 10
            shortcut = True
    if current_instruction == 13:
        can_take_shortcut = True
        for i in [13, 14, 15]:
            if i in toggled_instructions:
                can_take_shortcut = False
        if can_take_shortcut:
            registers['c'] = 2* registers['c']
            registers['d'] = 0
            current_instruction = 16
            shortcut = True

    if not shortcut:

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
                else:
                    print("unknown instruction to toggle")
                    exit(1)

                instructions[toggle_instruction_index] = instruction
            current_instruction += 1
        else:
            print("unknown instruction")
            exit(1)


print(registers['a'])

