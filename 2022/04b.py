import file_loader
import re

input_string = file_loader.get_input()


count = 0
for line in input_string.splitlines():
    a, b, x, y = [int(z) for z in re.split("[-,]", line)]
    if (b < x) or (y < a):
        pass
    else:
        count += 1
print(count)
