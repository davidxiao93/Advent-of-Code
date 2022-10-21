from typing import List, Tuple
from collections import namedtuple

input = """3,225,1,225,6,6,1100,1,238,225,104,0,1002,92,42,224,1001,224,-3444,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1102,24,81,225,1101,89,36,224,101,-125,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,118,191,224,101,-880,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,68,94,225,1101,85,91,225,1102,91,82,225,1102,85,77,224,101,-6545,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,84,20,225,102,41,36,224,101,-3321,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1,188,88,224,101,-183,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1001,84,43,224,1001,224,-137,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1102,71,92,225,1101,44,50,225,1102,29,47,225,101,7,195,224,101,-36,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,374,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,389,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,434,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,226,226,224,102,2,223,223,1006,224,494,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,524,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,584,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,614,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,7,677,677,224,102,2,223,223,1005,224,644,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,659,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"""
int_codes = [int(x) for x in input.split(",")]

Param = namedtuple("Param", ["mode", "value"])

opcodes = {
    1: (3, "add"),
    2: (3, "multiply"),
    3: (1, "read-input"),
    4: (1, "write-output"),
    5: (2, "jump-if-true"),
    6: (2, "jump-if-false"),
    7: (3, "less-than"),
    8: (3, "equals"),
    99: (0, "halt")
}

def parse_instruction(int_codes: List[int], current_instruction: int) -> Tuple[str, List[Param]]:
    opcode = int_codes[current_instruction]%100
    if opcode not in opcodes:
        print("unknown opcode")
        exit(1)
    params = []
    parameter_mode = int_codes[current_instruction]//100
    for param_value in int_codes[current_instruction + 1:current_instruction + 1 + opcodes[opcode][0]]:
        param_mode = parameter_mode%10
        params.append(Param(param_mode, param_value))
        parameter_mode = parameter_mode // 10
    return opcodes[opcode][1], params

def read_param(int_codes: List[int], param: Param):
    if param.mode == 0:
        if param.value < 0:
            print("Warning, param value is negative! Continuing as though this isnt a problem")
        return int_codes[param.value]
    elif param.mode == 1:
        return param.value
    else:
        print("Unknown param mode")
        exit(1)

def run(int_codes: List[int], inputs_queue: List[int]) -> List[int]:
    current_instruction = 0
    outputs_queue = []
    while True:
        opcode, params = parse_instruction(int_codes, current_instruction)
        jumped = False
        if opcode == "add":
            int_codes[params[2].value] = read_param(int_codes, params[0]) + read_param(int_codes, params[1])
        elif opcode == "multiply":
            int_codes[params[2].value] = read_param(int_codes, params[0]) * read_param(int_codes, params[1])
        elif opcode == "read-input":
            if len(inputs_queue) == 0:
                print("Empty input queue")
                exit(1)
            int_codes[params[0].value] = inputs_queue.pop(0)
        elif opcode == "write-output":
            outputs_queue.append(read_param(int_codes, params[0]))
        elif opcode == "jump-if-true":
            if read_param(int_codes, params[0]) != 0:
                current_instruction = read_param(int_codes, params[1])
                jumped = True
        elif opcode == "jump-if-false":
            if read_param(int_codes, params[0]) == 0:
                current_instruction = read_param(int_codes, params[1])
                jumped = True
        elif opcode == "less-than":
            int_codes[params[2].value] = 1 if read_param(int_codes, params[0]) < read_param(int_codes, params[1]) else 0
        elif opcode == "equals":
            int_codes[params[2].value] = 1 if read_param(int_codes, params[0]) == read_param(int_codes, params[1]) else 0
        elif opcode == "halt":
            break
        else:
            print("unknown opcode")
            exit(1)
        if not jumped:
            current_instruction += 1 + len(params)
    return outputs_queue


outputs = run(int_codes, [5])
print(outputs[0])
