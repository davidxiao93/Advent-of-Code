import file_loader

input_string = file_loader.get_input()

visited = dict()

for line in input_string.splitlines():
    x1, y1, x2, y2 = [int(i.strip()) for i in line.replace("->", ",").split(",")]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, y) not in visited:
                visited[(x1, y)] = 0
            visited[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if (x, y1) not in visited:
                visited[(x, y1)] = 0
            visited[(x, y1)] += 1

count = 0
for key, value in visited.items():
    if value > 1:
        count += 1

print(count)