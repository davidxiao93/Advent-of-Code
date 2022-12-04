import file_loader
import re

input_string = file_loader.get_input()


count = 0
for line in input_string.splitlines():
    a, b, x, y = [int(z) for z in re.split("[-,]", line)]
    if (a <= x and y <= b) or (x <= a and b <= y):
        count += 1
print(count)
