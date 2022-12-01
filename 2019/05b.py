from typing import List, Tuple
from collections import namedtuple

import file_loader

input_string = file_loader.get_input()
int_codes = [int(x) for x in input_string.split(",")]

Param = namedtuple("Param", ["mode", "value"])

opcodes = {
    1: (3, "add"),
    2: (3, "multiply"),
    3: (1, "read-input_string"),
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
        elif opcode == "read-input_string":
            if len(inputs_queue) == 0:
                print("Empty input_string queue")
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
