import file_loader

input_string = file_loader.get_input()

# input_string = """b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10"""

registers = {}


instructions = input_string.splitlines()

highest = 0

for instruction in instructions:
    words = instruction.split()
    register = words[0]
    direction = 1 if words[1] == "inc" else -1
    distance = int(words[2])
    cregister = words[4]
    coperator = words[5]
    cvalue = int(words[6])

    if register not in registers:
        registers[register] = 0

    if cregister not in registers:
        registers[cregister] = 0

    if coperator == ">":
        is_conditon_true = registers[cregister] > cvalue
    elif coperator == "<":
        is_conditon_true = registers[cregister] < cvalue
    elif coperator == ">=":
        is_conditon_true = registers[cregister] >= cvalue
    elif coperator == "<=":
        is_conditon_true = registers[cregister] <= cvalue
    elif coperator == "==":
        is_conditon_true = registers[cregister] == cvalue
    elif coperator == "!=":
        is_conditon_true = registers[cregister] != cvalue
    else:
        print("unknown operator", coperator)
        is_conditon_true = False

    if is_conditon_true:
        registers[register] += direction * distance
        if registers[register] > highest:
            highest = registers[register]

print(highest)

