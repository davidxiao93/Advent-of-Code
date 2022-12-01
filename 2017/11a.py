import file_loader

input_string = file_loader.get_input()

# key insight, order doesnt actually matter. The end destination is the same

direction_steps = {
    "nw": 0,
    "n": 0,
    "ne": 0,
    "se": 0,
    "s": 0,
    "sw": 0
}
directions = input_string.split(",")
for direction in directions:
    direction_steps[direction] += 1

simplifications = {
    ("n", "s"): [],
    ("ne", "sw"): [],
    ("nw", "se"): [],
    ("ne", "s"): ["se"],
    ("nw", "s"): ["sw"],
    ("n", "se"): ["ne"],
    ("n", "sw"): ["nw"],
    ("se", "sw"): ["s"],
    ("ne", "nw"): ["n"]
}

has_changed = True
while has_changed:
    has_changed = False
    # print(direction_steps)
    for (a, b), rs in simplifications.items():
        if direction_steps[a] > 0 and direction_steps[b] > 0:
            has_changed = True
            direction_steps[a] -= 1
            direction_steps[b] -= 1
            for r in rs:
                direction_steps[r] += 1
    if sum(direction_steps.values()) == 0:
        break

# print(direction_steps)
print(sum(direction_steps.values()))


