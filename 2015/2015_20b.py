input = 36000000

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
while True:
    count = num_presents(house)
    print(house, count)
    if count > input:
        break

    house += 1
