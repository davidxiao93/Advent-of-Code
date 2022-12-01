import re

import file_loader

input_string = file_loader.get_input()

results = re.findall("-?\d+", input_string)

print(sum([int(x) for x in results]))