from typing import Set, Tuple, List

import file_loader

input_string = file_loader.get_input()

# input_string = """5-8
# 0-2
# 4-7"""

from collections import namedtuple

Bound = namedtuple("Bound", ["lower", "upper"])

bounds = []


def merge_bounds(a: Bound, b: Bound):
    return Bound(lower=min(a.lower, b.lower), upper=max(a.upper, b.upper))

def overlapping(a: Bound, b:Bound):
    return a.upper >= b.lower - 1

def sort_bounds_by_lower(bs: List[Bound]):
    return sorted(bs, key=lambda b: b.lower)


for line in input_string.splitlines():
    lower_bound, upper_bound = [int(x) for x in line.split("-", 1)]
    bounds.append(Bound(lower=lower_bound, upper=upper_bound))

bounds = sort_bounds_by_lower(bounds)


index = 0
while index < len(bounds) - 1:
    a = bounds[index]
    b = bounds[index + 1]
    if overlapping(a, b):
        m = merge_bounds(a, b)
        bounds[index] = m
        bounds.pop(index+1)
    else:
        index += 1





print(bounds[0].upper + 1)


