import file_loader

input_string = file_loader.get_input()

input_string = [int(x) for x in input_string.splitlines()]

left, right = input_string[:-3], input_string[3:]

count = 0

for i in range(len(left)):
    if left[i] < right[i]:
        count += 1

print(count)

