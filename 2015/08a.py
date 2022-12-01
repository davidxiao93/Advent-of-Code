import file_loader

input_string = file_loader.get_input()

import re

count = 0
for l in input_string.split("\n"):
    line = l.strip()
    code = len(line)
    memory = len(
        re.sub("\\\\x[0-9a-fA-F][0-9a-fA-F]", "a",
        line[1:-1]
                 .replace("\\\\", "\\")
                 .replace("\\\"", "\"")
                 ))

    count += code
    count -= memory

print(count)