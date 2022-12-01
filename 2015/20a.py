import file_loader

input_string = file_loader.get_input()

# number of presents for a house = sum(house number distinct factors including itself and 1) * 10

import math

def num_presents(h):
    sum_factors = set()
    for i in range(1, math.floor(math.sqrt(h)) + 1):
        if h % i == 0:
            sum_factors.add(i)
            sum_factors.add(int(h/i))
    return sum(sum_factors) * 10


from itertools import combinations

def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list)+1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs


house = 1
target = int(input_string)
while True:
    count = num_presents(house)
    if count > target:
        print(house)
        break

    house += 1