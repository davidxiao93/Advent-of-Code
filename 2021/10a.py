import file_loader

input_string = file_loader.get_input()



open_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

score = 0

for line in input_string.splitlines():
    next_expected = []
    for c in line:
        if c in open_close:
            next_expected.append(open_close.get(c))
        elif c == next_expected[-1]:
            next_expected.pop()
        else:
            # corrupt
            score += scores.get(c)
            break

print(score)
