import file_loader

input_string = file_loader.get_input()

points = dict()
for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        points[(x, y)] = int(c)

risk_level = 0

for p, h in points.items():
    count = 0
    for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        neighbour = points.get((p[0] + x, p[1] + y), 10)
        if neighbour > h:
            count += 1
    if count == 4:
        risk_level += 1
        risk_level += h

print(risk_level)