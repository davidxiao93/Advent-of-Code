import file_loader

input_string = file_loader.get_input()

num_digits = len(input_string.splitlines()[0])

zeros_count = [0]*num_digits
ones_count = [0]*num_digits

for line in input_string.splitlines():
    for position, value in enumerate(line):
        if int(value) == 0:
            zeros_count[position] += 1
        else:
            ones_count[position] += 1

gamma = 0
epsilon = 0

for i in range(num_digits):
    if zeros_count[i] > ones_count[i]:
        gamma = gamma * 2
        epsilon = epsilon * 2 + 1
    else:
        gamma = gamma * 2 + 1
        epsilon = epsilon * 2

print(gamma * epsilon)

