from typing import List

import file_loader

input_string = file_loader.get_input()


# input_string = r"""/->-\
# |   |  /----\
# | /-+--+-\  |
# | | |  | v  |
# \-+-/  \-+--/
#   \------/ """
#
# input_string = r"""/>-<\
# |   |
# | /<+-\
# | | | v
# \>+</ |
#   |   ^
#   \<->/"""


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


up = Point(x = 0, y = -1)
down = Point(x = 0, y = 1)
left = Point(x = -1, y = 0)
right = Point(x = 1, y = 0)
directions = [up, right, down, left]

def add_point(p: Point, q: Point):
    return Point(x=p.x+q.x, y=p.y+q.y)

class Cart:
    def __init__(self, tracks, position: Point, direction: Point):
        self.tracks = tracks
        self.position = position
        self.direction = direction
        self.intersection_count = 0

    def turn_left(self):
        self.direction = directions[
            (directions.index(self.direction) - 1) % 4
        ]

    def turn_right(self):
        self.direction = directions[
            (directions.index(self.direction) + 1) % 4
        ]

    def move(self):
        self.position = add_point(self.position, self.direction)
        track = self.tracks[self.position.y][self.position.x]
        if track == "|":
            if self.direction != up and self.direction != down:
                print("wtf: invalid movement into |")
                exit(1)
        elif track == "-":
            if self.direction != left and self.direction != right:
                print("wtf: invalid movement into -")
                exit(1)
        elif track == "/":
            if self.direction == down or self.direction == up:
                self.turn_right()
            elif self.direction == left or self.direction == right:
                self.turn_left()
        elif track == "\\":
            if self.direction == down or self.direction == up:
                self.turn_left()
            elif self.direction == left or self.direction == right:
                self.turn_right()
        elif track == "+":
            if self.intersection_count == 0:
                self.turn_left()
            elif self.intersection_count == 2:
                self.turn_right()
            self.intersection_count  = (self.intersection_count + 1) % 3
        else:
            print("wtf, unknown track")
            exit(1)


tracks = []
carts = []
for y, line in enumerate(input_string.splitlines()):
    track_row = []
    for x, c in enumerate(line):
        if c not in ["^", "v", "<", ">"]:
            track_row.append(c)
        else:
            if c == "^":
                direction = up
                track_replacement = "|"
            elif c == "v":
                direction = down
                track_replacement = "|"
            elif c == ">":
                direction = right
                track_replacement = "-"
            else:
                direction = left
                track_replacement = "-"
            track_row.append(track_replacement)
            carts.append(
                Cart(tracks, Point(x, y), direction)
            )
    tracks.append(track_row)


def pretty_print(tracks, carts: List[Cart]):
    cart_positions = {cart.position: cart for cart in carts}
    for y, line in enumerate(tracks):
        row = []
        for x, t in enumerate(line):
            if Point(x, y) not in cart_positions:
                row.append(t)
            else:
                direction = cart_positions[Point(x, y)].direction
                if direction == up:
                    row.append("^")
                elif direction == right:
                    row.append(">")
                elif direction == down:
                    row.append("v")
                else:
                    row.append("<")
        print("".join(row))

def is_collision(carts: List[Cart], carts_to_remove: List[Cart]):
    # returns carts to remove
    seen = {}
    for cart in carts:
        if cart in carts_to_remove:
            continue
        if cart.position in seen:
            return [seen[cart.position], cart]
        seen[cart.position] = cart
    return []

def advance_carts(carts: List[Cart]):
    # returns (x,y) of crash if there is crash. None otherwise
    carts = sorted(carts, key=lambda cart: (cart.position.y, cart.position.x))
    carts_to_remove = []
    for cart in carts:
        cart.move()
        carts_to_remove += is_collision(carts, carts_to_remove)
    for cart in carts_to_remove:
        carts.remove(cart)
    return carts

# pretty_print(tracks, carts)
while len(carts) > 1:
    carts = advance_carts(carts)
    # print("----")
    # pretty_print(tracks, carts)

if len(carts) == 0:
    print("no carts left")
else:
    print(",".join([str(a) for a in carts[0].position]))








