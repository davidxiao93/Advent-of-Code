import file_loader

input_string = file_loader.get_input()

half_index = int(len(input_string) / 2)
print(sum([int(a) if a == b else 0 for a, b in zip(input_string, input_string[half_index:] + input_string[:half_index])]))
