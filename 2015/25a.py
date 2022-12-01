import file_loader

input_string = file_loader.get_input()

target_row = int(input_string.split()[-3][:-1])
target_column = int(input_string.split()[-1][:-1])
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