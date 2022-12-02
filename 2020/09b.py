import file_loader

input_string = file_loader.get_input()
preamble = 25
target = 1639024365 # from part a

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
# target = 127 # from part a

values = [int(x) for x in input_string.split()]

lower_bound = 0
upper_bound = 0
sum = values[0]

is_found = False

while sum != target:
    if lower_bound == upper_bound or sum < target:
        upper_bound += 1
        sum += values[upper_bound]
    elif sum > target:
        sum -= values[lower_bound]
        lower_bound += 1


s = values[lower_bound: upper_bound + 1]
print(min(s) + max(s))