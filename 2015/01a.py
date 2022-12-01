import file_loader

input_string = file_loader.get_input()

print(input_string.count('(') - input_string.count(')'))
