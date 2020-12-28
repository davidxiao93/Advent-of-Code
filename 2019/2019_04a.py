input = """109165-576723"""
lower_bound = int(input.split("-")[0])
upper_bound = int(input.split("-")[1])

def is_valid(v):
    if v < lower_bound or v > upper_bound:
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
for i in range(lower_bound, upper_bound + 1):
    if is_valid(i):
        count += 1

print(count)
