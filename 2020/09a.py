import file_loader

input_string = file_loader.get_input()
preamble = 25


# input_string = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576"""
# preamble = 5

values = [int(x) for x in input_string.split()]

from itertools import combinations

def check_valid(nums, target):
    for a, b in combinations(nums, 2):
        if target == a + b and a != b:
            return True
    print(target)
    return False


is_valid = True
i = preamble
while is_valid and i + 1 < len(values):
    v = values[i-preamble: i]
    next = values[i]
    is_valid = check_valid(v, next)
    i += 1

if is_valid:
    print("wtf")