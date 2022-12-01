import file_loader

input_string = file_loader.get_input()
image_height = 6
image_width = 25

layers = []
while len(input_string) != 0:
    layer = []
    for y in range(image_height):
        layer.append([int(x) for x in input_string[:image_width]])
        input_string = input_string[image_width:]
    layers.append(layer)


for y in range(image_height):
    row = []
    for x in range(image_width):
        current_colour = 2
        for l in layers:
            if l[y][x] != 2:
                current_colour = l[y][x]
            if current_colour != 2:
                break
        row.append(current_colour)
    print("".join(["#" if v == 1 else "." for v in row]))

