import file_loader

input_string = file_loader.get_input()

strength = 0
x = 1
cycle = 0


def update_strength(strength, x, cycle):
    if cycle % 40 == 20:
        return strength + cycle * x
    return strength

for line in input_string.splitlines():
    if line == "noop":
        cycle += 1
        strength = update_strength(strength, x, cycle)
    elif line.startswith("addx"):
        for i in range(2):
            cycle += 1
            strength = update_strength(strength, x, cycle)
        x += int(line.split()[1])

print(strength)

