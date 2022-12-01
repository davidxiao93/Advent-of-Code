import file_loader

input_string = file_loader.get_input()

input_string = [int(x) for x in input_string.splitlines()]

sorted_input = sorted(input_string)
pairs = {}

for x in sorted_input:
    if 2020 - x in pairs:
        y = pairs[2020-x][0][0]
        z = pairs[2020-x][0][1]
        print(x * y * z)
        exit(0)
    for y in sorted_input:
        if x > y:
            continue
        if x+y not in pairs:
            pairs[x+y] = []
        # print("adding ", x+y, " with ", x, " ", y)
        pairs[x+y].append((x,y))


