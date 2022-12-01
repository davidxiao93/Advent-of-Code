import file_loader

input_string = file_loader.get_input()
target_rows = 40


SAFE = "."
TRAP = "^"

rows = [
    input_string
]

for i in range(1, target_rows):
    last_row = SAFE + rows[i - 1] + SAFE
    new_row = ""
    for a, b, c in zip(last_row, last_row[1:], last_row[2:]):
        if (a == b == TRAP and c == SAFE) \
            or (a == SAFE and b == c == TRAP) \
            or (a == TRAP and b == c == SAFE) \
            or (a == b == SAFE and c == TRAP):
            new_row += TRAP
        else:
            new_row += SAFE

    rows.append(new_row)

count = 0
for row in rows:
    count += row.count(SAFE)

print(count)