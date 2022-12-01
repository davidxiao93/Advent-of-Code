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
    least_count = 1000000
    least_letter = ''
    for k, v in d.items():
        if v < least_count:
            least_count = v
            least_letter = k
    message += least_letter

print(message)