import file_loader

input_string = file_loader.get_input()

from itertools import combinations
from typing import Set
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
Rect = namedtuple("Rect", ["id", "ul", "dr"])

rectangles = []
for line in input_string.splitlines():
    id_str, s = line.split("@")
    id = int(id_str[1:])
    l, r = [t.strip() for t in s.split(":")]
    x1, y1 = [int(t) for t in l.split(",")]
    w, h = [int(t) for t in r.split("x")]
    x2 = x1 + w
    y2 = y1 + h
    rectangles.append(Rect(
        id=id,
        ul = Point(x1, y1),
        dr = Point(x2, y2)
    ))


def is_overlapping_dim(a, b, x, y, l) -> bool:
    if l(b) < l(x):
        return False
    if l(y) < l(a):
        return False
    for i in range(min(l(a), l(x)), 1 + max(l(b), l(y))):
        if l(a) <= i < l(b) and l(x) <= i < l(y):
            return True

    return False


def get_overlapping_ids(r: Rect, s:Rect) -> Set[int]:
    if is_overlapping_dim(r.ul, r.dr, s.ul, s.dr, lambda p: p.x) and is_overlapping_dim(r.ul, r.dr, s.ul, s.dr, lambda p: p.y):
        return {r.id, s.id}
    return set()


ids_with_overlap = set()
for r, s in combinations(rectangles, 2):
    ids_with_overlap |= get_overlapping_ids(r, s)

ids_with_no_overlap = {r.id for r in rectangles} - ids_with_overlap

print(next(iter(ids_with_no_overlap)))



