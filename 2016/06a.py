import file_loader

input_string = file_loader.get_input()

positions = {

}

for line in input_string.splitlines():
    for i, c in enumerate(line):
        if i not in positions:
            positions[i] = {}
        if c not in positions[i]:
            positions[i][c] = 0
        positions[i][c] += 1

message = ""
for position, d in positions.items():
    most_count = 0
    most_letter = ''
    for k, v in d.items():
        if v > most_count:
            most_count = v
            most_letter = k
    message += most_letter

print(message)