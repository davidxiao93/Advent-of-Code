def is_valid(v):
    if v < 109165 or v > 576723:
        return False
    v_list = list(str(v))

    """
    Because the digits must not be decreasing, the only way a "2" can appear is after any 1s and before
    any 3s
    i.e. we can simply count them to make sure there are exactly two of them
    """
    digit_count = {}
    for d in v_list:
        if d not in digit_count:
            digit_count[d] = 0
        digit_count[d] += 1

    if 2 not in digit_count.values():
        return False


    if v_list != sorted(v_list):
        return False
    return True

count = 0
for i in range(109165, 576723 + 1):
    if is_valid(i):
        count += 1

print(count)
