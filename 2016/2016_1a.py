input = """L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"""



from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

directions = [
    Point(x=0, y=1), # North
    Point(x=1, y=0), # East
    Point(x=0, y=-1), # South
    Point(x=-1, y=0) # West
]

current_direction = 0

def turn_left(cd):
    cd -= 1
    if cd < 0:
        cd += 4
    return cd

def turn_right(cd):
    cd += 1
    if cd >= 4:
        cd -= 4
    return cd

current_pos = Point(x=0, y=0)

def move(cp: Point, d: int):
    return Point(x=cp.x + d*directions[current_direction].x,
                 y=cp.y + d*directions[current_direction].y)


input = input.replace(",", "")

for i in input.split():
    if i[0] == "L":
        current_direction = turn_left(current_direction)
    elif i[0] == "R":
        current_direction = turn_right(current_direction)
    else:
        print("Error, cannot understand instruction")
        exit(1)

    d = int(i[1:])
    current_pos = move(current_pos, d)

print(current_pos)
print(abs(current_pos.x) + abs(current_pos.y))

