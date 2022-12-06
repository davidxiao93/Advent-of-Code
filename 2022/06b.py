import file_loader

input_string = file_loader.get_input()

marker_length = 14

last_chars = []
for i, c in enumerate(input_string):
    last_chars.append(c)
    last_chars = last_chars[-1 * marker_length:]
    if marker_length == len(set(last_chars)):
        print(i + 1)
        break
