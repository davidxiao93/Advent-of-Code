from typing import List

import file_loader

input_string = file_loader.get_input()
target = 5


import math

def rotate2(t):
    # 0 1 -> 2 0
    # 2 3    3 1
    return (t[2], t[0], t[3], t[1])

def flip2(t):
    # 0 1 -> 1 0
    # 2 3 -> 3 2
    return (t[1], t[0], t[3], t[2])

def rotate3(t):
    # 0 1 2    6 3 0
    # 3 4 5 -> 7 4 1
    # 6 7 8    8 5 2
    return (t[6], t[3], t[0], t[7], t[4], t[1], t[8], t[5], t[2])

def flip3(t):
    # 0 1 2    2 1 0
    # 3 4 5 -> 5 4 3
    # 6 7 8    8 7 6
    return (t[2], t[1], t[0], t[5], t[4], t[3], t[8], t[7], t[6])

enhancements = {}

for line in input_string.splitlines():
    l, r = [tuple(s.strip().replace("/", "")) for s in line.split("=>", 1)]

    if len(l) == 4:
        rotate = rotate2
        flip = flip2
    else:
        rotate = rotate3
        flip = flip3

    for i in range(2):
        for j in range(4):
            enhancements[l] = r
            l = rotate(l)
        l = flip(l)





def enhance_tuple(t):
    return enhancements[t]


def grid_to_tuples(grid: List[str]):
    tuple_sides = 3
    if len(grid) % 2 == 0:
        tuple_sides = 2
    tuples = []
    for ty in range(int(len(grid) / tuple_sides)):
        ts = [()] * int(len(grid) / tuple_sides)
        for y, r in enumerate(grid[ty * tuple_sides: ty * tuple_sides + tuple_sides]):
            for i in range(0, len(r), tuple_sides):
                ts[(int(i/tuple_sides))] = ts[(int(i/tuple_sides))] + tuple(r[i: i + tuple_sides])
        tuples += ts
    return tuples


def tuples_to_grid(tuples) -> List[str]:
    sides = int(math.sqrt(len(tuples)))
    tuple_sides = int(math.sqrt(len(tuples[0])))
    grid = []
    for i in range(sides):
        ts = tuples[sides * i: sides * i + sides]
        tuple_row = [""] * tuple_sides
        for t in ts:
            for y in range(tuple_sides):
                for x in range(tuple_sides):
                    tuple_row[y] += t[y*tuple_sides + x]
        grid += tuple_row
    return grid



def enhance(grid):
    tuples = grid_to_tuples(grid)
    tuples = [enhance_tuple(t) for t in tuples]
    grid = tuples_to_grid(tuples)
    return grid


def pretty_print_grid(grid):
    for r in grid:
        print(r)


def number_lights_on(grid):
    return sum([r.count("#") for r in grid])

# input_string = """../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#"""
# target = 2

grid = [".#.", "..#", "###"]
for i in range(target):
    grid = enhance(grid)
# pretty_print_grid(grid)

print(str(number_lights_on(grid)))













