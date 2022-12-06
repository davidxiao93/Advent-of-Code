import file_loader

input_string = file_loader.get_input()

last_chars = []
for i, c in enumerate(input_string):
    last_chars.append(c)
    last_chars = last_chars[-4:]
    if 4 == len(set(last_chars)):
        print(i + 1)
        break
