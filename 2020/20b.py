from typing import List, Set

import file_loader

input_string = file_loader.get_input()

# input_string = """Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
#
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
#
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
#
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
#
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
#
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
#
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
#
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
#
# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###..."""

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)

class Image:
    def __init__(self, contents: List[List[str]]):
        self.contents = contents

    def rotate_right(self):
        # impressive rotation from https://stackoverflow.com/a/8421412
        self.contents = list(zip(*self.contents[::-1]))

    def flip_left_right(self):
        self.contents = [
            line[::-1]
            for line in self.contents
        ]

    def flip_top_botton(self):
        self.contents = self.contents[::-1]

    def pretty_print(self):
        print("-------")
        print("\n".join([
            "".join(row)
            for row in self.contents
        ]))
        print("-------")


class Tile:
    def __init__(self, tile_str):
        lines = tile_str.splitlines()
        self.id = int(lines[0][5:-1])
        ## All edges are clockwise
        self.edges = [
            lines[1],  # top edge
            "".join([s[-1] for s in lines[1:]]),  # right edge
            lines[-1][::-1],  # bottom edge
            "".join([s[0] for s in lines[:0:-1]])  # left edge
        ]
        self.image = Image([
            list(line[1:-1])
            for line in lines[2:-1]
        ])

    def rotate_right(self):
        self.edges = [self.edges[-1]] + self.edges[:-1]
        self.image.rotate_right()

    def flip_left_right(self):
        self.edges = [
            self.edges[0][::-1],
            self.edges[3][::-1],
            self.edges[2][::-1],
            self.edges[1][::-1]
        ]
        self.image.flip_left_right()

    def flip_top_bottom(self):
        self.edges = [
            self.edges[2][::-1],
            self.edges[1][::-1],
            self.edges[0][::-1],
            self.edges[3][::-1]
        ]
        self.image.flip_top_botton()

    def rotate(self, my_edge, other_edge):
        # other edge is fixed.
        while (my_edge - other_edge) % 4 != 2:
            self.rotate_right()
            my_edge = (my_edge + 1) % 4
        # handle flipping if needed
        return my_edge

    def set_position(self, position: Point):
        self.position = position


tiles = set()

for tile_str in input_string.split("\n\n"):
    tiles.add(Tile(tile_str))


tile_size = len(next(iter(tiles)).image.contents)

"""
I will make the assumption that the puzzle creator is nice
and that each edge has exactly one matching edge elsewhere

Lets confirm or disprove this
"""

edge_counts = {}
for tile in tiles:
    for edge in tile.edges:
        if edge not in edge_counts:
            edge_counts[edge] = 0
        edge_counts[edge] += 1
        if edge[::-1] not in edge_counts:
            edge_counts[edge[::-1]] = 0
        edge_counts[edge[::-1]] += 1

assert(max(edge_counts.values()) == 2)

"""
Max common edges is 2, which means that each pair of connected tiles share an 
otherwise unique edge between them
"""

tiles_to_place = list(tiles)
start_tile = tiles_to_place.pop(0)
start_tile.set_position(Point(0,0))
position_to_tiles = {
    Point(0,0): start_tile
}
connected_tiles = { start_tile }
while len(tiles_to_place) != 0:
    new_tile = tiles_to_place.pop(0)
    # if tile can be connected, then create the connection.
    found = None
    for ni, new_edge in enumerate(new_tile.edges):
        for connected_tile in connected_tiles:
            for i, edge in enumerate(connected_tile.edges):
                if edge == new_edge or edge[::-1] == new_edge:
                    # found connection point
                    found = (connected_tile, i, ni)
                    break
            if found:
                break
        if found:
            break

    if found:
        connected_tile, i, ni = found
        new_i = new_tile.rotate(ni, i)
        # we want the edges to be reverse of each other
        # because the edges are going in opposite directions as they are on
        # opposite sides

        if new_tile.edges[new_i] == connected_tile.edges[i]:
            if new_i % 2 == 0:
                new_tile.flip_left_right()
            else:
                new_tile.flip_top_bottom()
        assert (new_tile.edges[new_i] == connected_tile.edges[i][::-1])
        if new_i == 0:
            # new_tile is below connected_tile
            d = Point(x=0, y=1)
        elif new_i == 1:
            # new_tile is to the left of connected_tile
            d = Point(x=-1, y=0)
        elif new_i == 2:
            # new_tile is above connected_tile
            d = Point(x=0, y=-1)
        else:
            # new_tile is to the right of connected_tile
            d = Point(x=1, y=0)
        new_position = add_point(connected_tile.position, d)
        new_tile.set_position(new_position)
        if new_position in position_to_tiles:
            print("oh dear")
            exit(1)
        position_to_tiles[new_position] = new_tile
        connected_tiles.add(new_tile)


    # otherwise put it back at the end of the list
    if not found and new_tile not in tiles_to_place:
        tiles_to_place.append(new_tile)


assert(len(position_to_tiles) == len(tiles))

"""
Now we have placed all the tiles, and orientated/flipped them as needed on the way
Time to join all the tiles
"""

min_y = min(tiles, key=lambda t: t.position.y).position.y
max_y = max(tiles, key=lambda t: t.position.y).position.y
min_x = min(tiles, key=lambda t: t.position.x).position.x
max_x = max(tiles, key=lambda t: t.position.x).position.x


rows = []
for y in range(min_y, max_y + 1):
    for i in range(tile_size):
        row = []
        for x in range(min_x, max_x + 1):
            tile = position_to_tiles[Point(x, y)]
            row += tile.image.contents[i]
        rows.append(row)



full_image = Image(rows)
# full_image.pretty_print()

"""
Image joined up, and ready to search for Nessy
"""


def search_image(image: Image, nessy: List[Point], max_x: int, max_y: int) -> int:
    contents = image.contents
    # image.pretty_print()
    nessy_count = 0
    for y in range(len(contents) - max_y):
        for x in range(len(contents[0]) - max_x):
            found = True
            for dx, dy in nessy:
                if contents[y+dy][x+dx] != "#":
                    found = False
            if found:
                # print(f"Found nessy at {x},{y}")
                nessy_count += 1
    if nessy_count > 0:
        # I assume the nessys are not overlapping
        return sum([
            row.count("#")
            for row in contents
        ]) - nessy_count * len(nessy)
    return -1

# Convert Nessy to a list of offsets at which we check for '#'
# Idea shamelessly stolen from a friend
monster_pattern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster_coords = []
max_x = 0
max_y = 0
for dy, line in enumerate(monster_pattern.splitlines()):
    for dx, c in enumerate(line):
        if c == '#':
            monster_coords.append(Point(dx, dy))
            max_x = max(dx, max_x)
            max_y = max(dy, max_y)



for flips in range(2):
    for rotations in range(4):
        rough_waters = search_image(full_image, monster_coords, max_x, max_y)
        if rough_waters > 0:
            # Found nessys. We are done.
            print(rough_waters)
            exit(0)
        full_image.rotate_right()
    full_image.flip_left_right()




