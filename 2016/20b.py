from typing import Set, Tuple, List

import file_loader

input_string = file_loader.get_input()
max_allowed = 4294967295

# input_string = """5-8
# 0-2
# 4-7"""
# max_allowed=9

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



bounds_with_ends = [Bound(lower=-1, upper=-1)] + bounds + [Bound(lower=max_allowed+1, upper=max_allowed+1)]
allowed_bounds = []
for x, y in zip(bounds_with_ends, bounds_with_ends[1:]):
    if x.upper + 1 <= y.lower - 1:
        allowed_bounds.append(Bound(lower=x.upper + 1, upper=y.lower-1))

count = 0
for a in allowed_bounds:
    count += a.upper - a.lower + 1

print(count)


