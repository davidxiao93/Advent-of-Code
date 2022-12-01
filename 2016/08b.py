import file_loader

input_string = file_loader.get_input()


def rotate(l, q):
    q = q % len(l)
    return l[-1 * q:] + l[:-1 * q]


grid = [
    [0] * 50,
    [0] * 50,
    [0] * 50,
    [0] * 50,
    [0] * 50,
    [0] * 50
]



def rect_a_b(grid, a, b):
    for y in range(b):
        for x in range(a):
            grid[y][x] = 1
    return grid

def rotate_row(grid, row, q):
    grid[row] = rotate(grid[row], q)
    return grid

def rotate_column(grid, column, q):
    c = [r[column] for r in grid]
    c = rotate(c, q)
    for i, row in enumerate(grid):
        row[column] = c[i]
    return grid

for line in input_string.splitlines():
    s = line.split()
    if s[0] == "rect":
        a, b = s[1].split("x")
        grid = rect_a_b(grid, int(a), int(b))
    elif s[1] == "column":
        r = int(s[2].split("=")[-1])
        q = int(s[-1])
        grid = rotate_column(grid, r, q)
    elif s[1] == "row":
        r = int(s[2].split("=")[-1])
        q = int(s[-1])
        grid = rotate_row(grid, r, q)
    else:
        print("instruction not understood")
        exit(1)

for row in grid:
    print("".join(["#" if x == 1 else " " for x in row]))

"""
Note from future David:
I'm not OCRing this answer
"""

