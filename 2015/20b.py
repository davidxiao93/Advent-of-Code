import file_loader

input_string = file_loader.get_input()

import math

def num_presents(h):
    sum_factors = set()
    for i in range(1, math.floor(math.sqrt(h)) + 1):
        if h % i == 0:
            sum_factors.add(i)
            sum_factors.add(int(h/i))
    sum_factors = {f for f in sum_factors if h / f <= 50 }
    return sum(sum_factors) * 11


house = 1
target = int(input_string)
while True:
    count = num_presents(house)
    if count > target:
        print(house)
        break

    house += 1
