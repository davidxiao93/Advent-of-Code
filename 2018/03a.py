import file_loader

input_string = file_loader.get_input()

from itertools import combinations
from typing import Set
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
Rect = namedtuple("Rect", ["ul", "dr"])

rectangles = []
for line in input_string.splitlines():
    _, s = line.split("@")
    l, r = [t.strip() for t in s.split(":")]
    x1, y1 = [int(t) for t in l.split(",")]
    w, h = [int(t) for t in r.split("x")]
    x2 = x1 + w
    y2 = y1 + h
    rectangles.append(Rect(
        ul = Point(x1, y1),
        dr = Point(x2, y2)
    ))


def get_overlaps_dim(a, b, x, y, l) -> Set[int]:
    ret = set()
    if l(b) < l(x):
        return ret
    if l(y) < l(a):
        return ret
    for i in range(min(l(a), l(x)), 1 + max(l(b), l(y))):
        if l(a) <= i < l(b) and l(x) <= i < l(y):
            ret.add(i)

    return ret


def get_overlaps(r: Rect, s:Rect) -> Set[Point]:
    xs = get_overlaps_dim(r.ul, r.dr, s.ul, s.dr, lambda p: p.x)
    ys = get_overlaps_dim(r.ul, r.dr, s.ul, s.dr, lambda p: p.y)
    ret = set()
    for x in xs:
        for y in ys:
            ret.add(Point(x, y))
    return ret


overlaps = set()
for r, s in combinations(rectangles, 2):
    overlaps |= get_overlaps(r, s)
print(len(overlaps))




