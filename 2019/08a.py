import file_loader

input_string = file_loader.get_input()
image_height = 6
image_width = 25

layers = {}
flat_layers = {}
layer_index = 1
while len(input_string) != 0:
    layer = []
    flat_layer = []
    for y in range(image_height):
        new_values = [int(x) for x in input_string[:image_width]]
        layer.append(new_values)
        flat_layer += new_values
        input_string = input_string[image_width:]
    layers[layer_index] = layer
    flat_layers[layer_index] = flat_layer
    layer_index += 1

min_zero_layer = min(flat_layers.items(), key=lambda e: e[1].count(0))[0]

print(flat_layers[min_zero_layer].count(1) * flat_layers[min_zero_layer].count(2))
