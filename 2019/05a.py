from typing import List, Tuple
from collections import namedtuple

import file_loader

input_string = file_loader.get_input()
int_codes = [int(x) for x in input_string.split(",")]

Param = namedtuple("Param", ["mode", "value"])

opcode_num_param = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    99: 0
}

def parse_instruction(int_codes: List[int], current_instruction: int) -> Tuple[int, List[Param]]:
    opcode = int_codes[current_instruction]%100
    if opcode not in opcode_num_param:
        print("unknown opcode")
        exit(1)
    params = []
    parameter_mode = int_codes[current_instruction]//100
    for param_value in int_codes[current_instruction + 1:current_instruction + 1 + opcode_num_param[opcode]]:
        param_mode = parameter_mode%10
        params.append(Param(param_mode, param_value))
        parameter_mode = parameter_mode // 10
    return opcode, params

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
        if opcode == 1:
            int_codes[params[2].value] = read_param(int_codes, params[0]) + read_param(int_codes, params[1])
        elif opcode == 2:
            int_codes[params[2].value] = read_param(int_codes, params[0]) * read_param(int_codes, params[1])
        elif opcode == 3:
            if len(inputs_queue) == 0:
                print("Empty input_string queue")
                exit(1)
            int_codes[params[0].value] = inputs_queue.pop(0)
        elif opcode == 4:
            outputs_queue.append(read_param(int_codes, params[0]))
        elif opcode == 99:
            break
        else:
            print("unknown opcode")
            exit(1)
        current_instruction += 1 + len(params)
    return outputs_queue


outputs = run(int_codes, [1])
print(outputs[-1])
