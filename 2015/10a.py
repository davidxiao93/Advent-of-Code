import file_loader

input_string = file_loader.get_input()


def look_say(s):
    output = ""

    current_char = s[0]

    current_count = 0

    for c in s:
        if c == current_char:
            current_count += 1
        else:
            output += str(current_count) + current_char
            current_char = c
            current_count = 1

    output += str(current_count) + current_char
    return output

s = input_string
for i in range(40):
    s = look_say(s)

print(len(s))
