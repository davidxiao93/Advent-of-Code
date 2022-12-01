import file_loader

input_string = file_loader.get_input()


"""
For part 1, only care about finding the corners
The question states "the outermost edges won't line up with any other tiles"
Therefore, the corners must be tiles that have two edges that cannot line up with other tiles

"""


tiles = [
]

for tile_str in input_string.split("\n\n"):
    lines = tile_str.splitlines()
    id = int(lines[0][5:-1])
    edges = (
        lines[1], # top edge
        "".join([s[-1] for s in lines[1:]]), # right edge
        lines[-1], # bottom edge
        "".join([s[0] for s in lines[1:]]) # left edge
    )
    tiles.append((id, edges))


corner_tile_ids = []

for tile in tiles:
    connectable_edge_count = 0
    for edge in tile[1]:
        matches_some_tile = False
        for other_tile in tiles:
            matches_tile = False
            if tile == other_tile:
                continue
            for other_edge in other_tile[1]:
                if edge == other_edge or edge[::-1] == other_edge:
                    matches_tile = True
                    break
            if matches_tile:
                matches_some_tile = True
                break
        if matches_some_tile:
            connectable_edge_count += 1
    if connectable_edge_count == 2:
        # must be corner
        corner_tile_ids.append(tile[0])

assert(len(corner_tile_ids) == 4)
print(corner_tile_ids[0] * corner_tile_ids[1] * corner_tile_ids[2] * corner_tile_ids[3])



