import file_loader

input_string = file_loader.get_input()

directions = input_string.split(",")

def get_distance(directions):
    direction_steps = {
        "nw": 0,
        "n": 0,
        "ne": 0,
        "se": 0,
        "s": 0,
        "sw": 0
    }
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
        for (a, b), rs in simplifications.items():
            if direction_steps[a] > 0 and direction_steps[b] > 0:
                has_changed = True
                direction_steps[a] -= 1
                direction_steps[b] -= 1
                for r in rs:
                    direction_steps[r] += 1
        if sum(direction_steps.values()) == 0:
            break

    return sum(direction_steps.values())



print(max([get_distance(directions[:i]) for i in range(1, len(directions))]))
