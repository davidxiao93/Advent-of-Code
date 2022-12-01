import file_loader

input_string = file_loader.get_input()



instructions = input_string.splitlines()

current_instruction = 0
acc = 0

visited_instructions = set()

while 0 <= current_instruction < len(instructions):

    if current_instruction in visited_instructions:
        print(acc)
        exit(0)
    visited_instructions.add(current_instruction)


    words = instructions[current_instruction].split()

    if words[0] == "nop":
        current_instruction += 1
    elif words[0] == "acc":
        acc += int(words[1])
        current_instruction += 1
    elif words[0] == "jmp":
        current_instruction += int(words[1])
    else:
        print("wtf")
        exit(1)

