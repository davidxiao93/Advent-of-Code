def is_valid(v):
    if v < 109165 or v > 576723:
        return False
    v_list = list(str(v))
    has_double = False
    for a, b in zip(v_list, v_list[1:]):
        if a == b:
            has_double = True
    if not has_double:
        return False
    if v_list != sorted(v_list):
        return False
    return True

count = 0
for i in range(109165, 576723 + 1):
    if is_valid(i):
        count += 1

print(count)
