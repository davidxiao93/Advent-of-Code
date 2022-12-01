import file_loader

input_string = file_loader.get_input()
target_rows = 400000


SAFE = "."
TRAP = "^"

rows = [
    input_string
]

row_cache = {}
def build_next_row(last_row):
    if last_row not in row_cache:
        old_row = SAFE + rows[i - 1] + SAFE
        new_row = ""
        for a, b, c in zip(old_row, old_row[1:], old_row[2:]):
            if (a == b == TRAP and c == SAFE) \
                    or (a == SAFE and b == c == TRAP) \
                    or (a == TRAP and b == c == SAFE) \
                    or (a == b == SAFE and c == TRAP):
                new_row += TRAP
            else:
                new_row += SAFE
        row_cache[last_row] = new_row

    return row_cache[last_row]

for i in range(1, target_rows):
    rows.append(build_next_row(rows[i - 1]))

count = 0
for row in rows:
    count += row.count(SAFE)

print(count)