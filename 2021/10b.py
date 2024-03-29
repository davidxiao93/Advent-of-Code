import file_loader

input_string = file_loader.get_input()


open_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

all_scores = []

for line in input_string.splitlines():
    next_expected = []
    line_score = 0
    is_corrupt = False
    for c in line:
        if c in open_close:
            next_expected.append(open_close.get(c))
        elif c == next_expected[-1]:
            next_expected.pop()
        else:
            is_corrupt = True
            break
    if not is_corrupt and len(next_expected) > 0:
        # incomplete
        # reverse as we want to calculate score from next brace onwards
        next_expected.reverse()
        for r in next_expected:
            line_score = line_score * 5 + scores.get(r)
        all_scores.append(line_score)


print(sorted(all_scores)[int((len(all_scores) - 1)/2)])
