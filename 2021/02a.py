import file_loader

input_string = file_loader.get_input()
input_string = [(s.split()[0], int(s.split()[1])) for s in input_string.splitlines()]

x = 0
y = 0

for command in input_string:
    if command[0] == "forward":
        x += command[1]
    elif command[0] == "down":
        y += command[1]
    elif command[0] == "up":
        y -= command[1]

print(x*y)
