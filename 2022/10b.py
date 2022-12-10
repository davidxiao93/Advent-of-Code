import file_loader

input_string = file_loader.get_input()

x = 1
cycle = 0
crt = ""
screen_width = 40


def get_addition(cycle, sprite_pixels, crt):
    if (cycle - 1) % screen_width in sprite_pixels:
        crt += "#"
    else:
        crt += "."
    if cycle % screen_width == 0:
        crt += "\n"
    return crt

for line in input_string.splitlines():
    sprite_pixels = {x - 1, x, x + 1}.intersection(range(40))

    if line == "noop":
        cycle += 1
        crt = get_addition(cycle, sprite_pixels, crt)
    elif line.startswith("addx"):
        for i in range(2):
            cycle += 1
            crt = get_addition(cycle, sprite_pixels, crt)
        x += int(line.split()[1])

print(crt)
