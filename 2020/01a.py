import file_loader

input_string = file_loader.get_input()

input_string = [int(x) for x in input_string.splitlines()]

for x in input_string:
    if 2020 - x in input_string:
        print(x*(2020-x))
        exit(0)