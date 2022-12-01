import file_loader

input_string = file_loader.get_input()

int_codes = [int(x) for x in input_string.split(",")]

int_codes[1] = 12
int_codes[2] = 2


i = 0
while True:
    o, a, b, c = int_codes[4*i: 4*i + 4]
    if o == 1:
        int_codes[c] = int_codes[a] + int_codes[b]
    elif o == 2:
        int_codes[c] = int_codes[a] * int_codes[b]
    elif o == 99:
        break
    i += 1

print(int_codes[0])