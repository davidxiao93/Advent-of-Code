import file_loader

input_string = file_loader.get_input()

pos = 0
for i, c in enumerate(input_string):
    if pos < 0:
        print(i)
        exit(0)
    if c == '(':
        pos += 1
    if c == ')':
        pos -= 1
