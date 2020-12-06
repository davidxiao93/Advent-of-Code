input = 36000000

# number of presents for a house = sum(house number distinct factors including itself and 1) * 10

import math

def num_presents(h):
    sum_factors = set()
    for i in range(1, math.floor(math.sqrt(h)) + 1):
        if h % i == 0:
            sum_factors.add(i)
            sum_factors.add(int(h/i))
    return sum(sum_factors) * 10

# print(num_presents(831601))
#
# exit()

from itertools import combinations

def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list)+1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs

# sub_factors_list = sub_lists([1, 2, 3, 5, 7, 11, 13, 17, 19])
# candidates = []
# for sub_factors in sub_factors_list:
#     product = 1
#     for f in sub_factors:
#         product *= f
#     candidates.append(product)
#
# candidates.sort()
#
# print(candidates)
#
# count = 0
# i = 0
# while count < input:
#     house_number = candidates[i]
#     count = num_presents(house_number)
#     i += 1
#     print(house_number, count) # 1385670 43545600


house = 1
while True:
    count = num_presents(house)
    print(house, count)
    if count > input:
        break

    house += 1