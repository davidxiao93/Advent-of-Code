import file_loader

input_string = file_loader.get_input()



instructions = input_string.splitlines()


def loop(instructions):
    """
    Returns tuple of
     - acc valu when either loop detected or program terminated
     - set of possible corrupt instruction indexes
     - boolean, true if loop detected
    """

    current_instruction = 0
    acc = 0

    corrupt_instruction_candidates = set()
    visited_instructions = set()

    while 0 <= current_instruction < len(instructions):

        if current_instruction in visited_instructions:
            return (acc, corrupt_instruction_candidates, True)
        visited_instructions.add(current_instruction)


        words = instructions[current_instruction].split()

        if words[0] == "nop":
            corrupt_instruction_candidates.add(current_instruction)
            current_instruction += 1
        elif words[0] == "acc":
            acc += int(words[1])
            current_instruction += 1
        elif words[0] == "jmp":
            corrupt_instruction_candidates.add(current_instruction)
            current_instruction += int(words[1])
        else:
            print("wtf")
            exit(1)

    return (acc, corrupt_instruction_candidates, False)

_, corrupt_candidates, _ = loop(instructions)

# these corrupt_candidates are the instructions for which
# should check if they are the corrupted one

for c in corrupt_candidates:
    new_instructions = instructions.copy()
    old_words = new_instructions[c].split()
    if old_words[0] == "nop":
        new_instructions[c] = "jmp " + old_words[1]
    elif old_words[0] == "jmp":
        new_instructions[c] = "nop " + old_words[1]
    else:
        print("wtf2")
        exit(1)

    acc, _, is_loop = loop(new_instructions)

    if is_loop:
        continue
    print(acc)
    break


