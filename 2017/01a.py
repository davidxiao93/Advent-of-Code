import file_loader

input_string = file_loader.get_input()

print(sum([int(a) if a == b else 0 for a, b in zip(input_string, input_string[1:] + input_string[:1])]))
