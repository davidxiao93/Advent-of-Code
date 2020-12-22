input = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"""
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
        if target == run([int(x) for x in input.split(",")], n, v):
            print(100*n + v)
            break