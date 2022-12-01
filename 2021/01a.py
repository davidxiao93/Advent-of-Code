import file_loader

input_string = file_loader.get_input()
input_string = [int(x) for x in input_string.splitlines()]

current, remaining = input_string[0], input_string[1:]

count = 0

for next in remaining:
    if next > current:
        count += 1
    current = next

print(count)