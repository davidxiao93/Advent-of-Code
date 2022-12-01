import file_loader

input_string = file_loader.get_input()

import re

count = 0
for l in input_string.split("\n"):
    line = l.strip()
    code = len(line)
    encoded = len(
        re.sub("\\\\x[0-9a-fA-F][0-9a-fA-F]", "aaaaa",
        line
                 .replace("\"", "aa")
                 .replace("\\", "aa")
                 )) + 2

    count += encoded
    count -= code

print(count)