import file_loader

input_string = file_loader.get_input()

memory = {}
or_mask = None
and_mask = None
for line in input_string.splitlines():
    if line.startswith("mask"):
        mask = line.split("=", 1)[1].strip()
        or_mask = int(mask.replace("X", "0"), 2)
        and_mask = int(mask.replace("X", "1"), 2)
    elif line.startswith("mem"):
        left, right = line.split("=")
        key = int(left.strip()[4:-1])
        original_value = int(right)
        memory[key] = (original_value | or_mask) & and_mask
    else:
        print("wtf, unknown input_string")
        exit(1)

print(sum(memory.values()))