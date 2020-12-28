input = """To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075."""

target_row = int(input.split()[-3][:-1])
target_column = int(input.split()[-1][:-1])
start = 20151125

def calc_next(n):
    return (n*252533) % 33554393

def triangle(n):
    return int(n * (n + 1) / 2)

def pos(row, col):
    return triangle(row + col - 2) + col

current = start
# print(pos(target_row, target_column))
for i in range(pos(target_row, target_column) - 1):
    current = calc_next(current)

print(current)