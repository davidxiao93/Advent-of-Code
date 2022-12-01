import file_loader

input_string = file_loader.get_input()

memory = {}
and_or_masks = None
for line in input_string.splitlines():
    if line.startswith("mask"):
        and_or_masks = []
        unfloating_masks = []
        mask = line.split("=", 1)[1].strip()
        mask = mask.replace("0", "Y") # Y is the new X
        xs = mask.count("X")
        ss = [format(i, 'b').zfill(xs) for i in range(2 ** xs)]
        for s in ss:
            new_mask = mask
            for i in range(xs):
                new_mask = new_mask.replace("X", s[i], 1)
            unfloating_masks.append(new_mask)
        for unfloating_mask in unfloating_masks:
            or_mask = int(unfloating_mask.replace("Y", "0"), 2)
            and_mask = int(unfloating_mask.replace("Y", "1"), 2)
            and_or_masks.append((and_mask, or_mask))
    elif line.startswith("mem"):
        left, right = line.split("=")
        key = int(left.strip()[4:-1])
        value = int(right)
        for and_mask, or_mask in and_or_masks:
            new_key = (key | or_mask) & and_mask
            memory[new_key] = value
    else:
        print("wtf, unknown input_string")
        exit(1)

print(sum(memory.values()))