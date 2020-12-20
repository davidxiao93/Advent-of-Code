

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)


geologic_index_dict = {}
erosion_level_dict = {}

def get_geologic_index(p: Point, target: Point) -> int:
    if p in geologic_index_dict:
        return geologic_index_dict[p]

    if p.x == 0 and p.y == 0:
        geologic_index_dict[p] = 0
    elif p.x == target.x and p.y == target.y:
        geologic_index_dict[p] = 0
    elif p.y == 0:
        geologic_index_dict[p] = p.x * 16807
    elif p.x == 0:
        geologic_index_dict[p] = p.y * 48271
    else:
        geologic_index_dict[p] = get_erosion_level(
            add_point(p, Point(-1, 0)), target
        ) * get_erosion_level(
            add_point(p, Point(0, -1)), target
        )
    return geologic_index_dict[p]

def get_erosion_level(p: Point, target: Point) -> int:
    if p in erosion_level_dict:
        return erosion_level_dict[p]

    geologic_index = get_geologic_index(p, target)
    erosion_level = (geologic_index + depth) % 20183
    erosion_level_dict[p] = erosion_level
    return erosion_level_dict[p]

def get_type(p: Point, target: Point) -> int:
    return get_erosion_level(p, target) % 3

def get_printable_type(p: Point, target: Point) -> str:
    type = get_type(p, target)
    if type == 0:
        # rocky
        return "."
    elif type == 1:
        # wet
        return "="
    else:
        # narrow
        return "|"


start = Point(0, 0)
target = Point(10, 715)
depth = 3339

# for y in range(16):
#     row = []
#     for x in range(16):
#         if Point(x, y) == start:
#             row.append("M")
#         elif Point(x, y) == target:
#             row.append("T")
#         else:
#             row.append(get_printable_type(Point(x, y), target, depth, geologic_index_dict, erosion_level_dict))
#     print("".join(row))

def get_risk_level(start: Point, target: Point) -> int:
    risk = 0
    for y in range(start.y, target.y + 1):
        for x in range(start.x, target.x + 1):
            p = Point(x, y)
            risk += get_type(p, target)
    return risk

print(get_risk_level(start, target))


