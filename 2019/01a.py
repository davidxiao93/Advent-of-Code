import file_loader

input_string = file_loader.get_input()

total_fuel = 0
for line in input_string.splitlines():
    mass = int(line)
    total_fuel += mass // 3
    total_fuel -= 2
print(total_fuel)