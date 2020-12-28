input = """154, 159
172, 84
235, 204
181, 122
161, 337
305, 104
128, 298
176, 328
146, 71
210, 87
341, 195
50, 96
225, 151
86, 171
239, 68
79, 50
191, 284
200, 122
282, 240
224, 282
327, 74
158, 289
331, 244
154, 327
317, 110
272, 179
173, 175
187, 104
44, 194
202, 332
249, 197
244, 225
52, 127
299, 198
123, 198
349, 75
233, 72
284, 130
119, 150
172, 355
147, 314
58, 335
341, 348
236, 115
185, 270
173, 145
46, 288
214, 127
158, 293
237, 311"""
target = 10000


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x=0, y=1)
down = Point(x=0, y=-1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

def add_point(p, q):
    return Point(p.x+q.x, p.y+q.y)

points = set()
for line in input.splitlines():
    words = line.split(",")
    x, y = [int(a) for a in words]
    points.add(Point(x, y))


def distance(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)


def is_close(p, points, target):
    count = 0
    for q in points:
        count += distance(p, q)
        if count >= target:
            return False
    return True


# find center.
# The center will always have the lowest sum of spokes

center_x = int(sum([p.x for p in points]) / len(points))
center_y = int(sum([p.y for p in points]) / len(points))

# Then search outwards.
# The region that fulfils the criteria of being sufficient close to all points must be a single
# contiguous area.
matching = set()
candiates = {Point(center_x, center_y)}
while len(candiates) != 0:
    next_candidate = candiates.pop()

    if is_close(next_candidate, points, target):
        matching.add(next_candidate)
        for d in [up, down, left, right]:
            new_candidate = add_point(next_candidate, d)
            if new_candidate not in matching and new_candidate not in candiates:
                candiates.add(new_candidate)

print(len(matching))







