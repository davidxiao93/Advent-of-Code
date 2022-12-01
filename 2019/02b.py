import file_loader

input_string = file_loader.get_input()
target = 19690720


def run(int_codes, noun, verb):
    int_codes[1] = noun
    int_codes[2] = verb
    current_instruction = 0
    while True:
        o = int_codes[current_instruction]
        if o == 1:
            a, b, c = int_codes[current_instruction + 1: current_instruction + 4]
            int_codes[c] = int_codes[a] + int_codes[b]
            current_instruction += 4
        elif o == 2:
            a, b, c = int_codes[current_instruction + 1: current_instruction + 4]
            int_codes[c] = int_codes[a] * int_codes[b]
            current_instruction += 4
        elif o == 99:
            break
        else:
            print("oh no")
            return -1
    return int_codes[0]

for n in range(100):
    for v in range(100):
        if target == run([int(x) for x in input_string.split(",")], n, v):
            print(100*n + v)
            break