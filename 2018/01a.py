import file_loader

input_string = file_loader.get_input()
print(sum(int(s) for s in input_string.splitlines()))