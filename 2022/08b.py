from typing import List, Tuple

import file_loader

input_string = file_loader.get_input()

trees = [
    [
        int(c) for c in line
    ] for line in input_string.splitlines()
]
max_x = len(trees)
max_y = len(trees[0])

def score_tree_direction(trees, x, y, dx, dy):
    tree_height = trees[x][y]
    cx = x + dx
    cy = y + dy
    score = 0
    while 0 <= cx < max_x and 0 <= cy < max_y:
        score += 1
        if trees[cx][cy] >= tree_height:
            break
        cx = cx + dx
        cy = cy + dy
    return score

def score_tree(trees, x, y):
    return score_tree_direction(trees, x, y, 0, 1) \
           * score_tree_direction(trees, x, y, 0, -1) \
           * score_tree_direction(trees, x, y, 1, 0) \
           * score_tree_direction(trees, x, y, -1, 0)

print(max([
    score_tree(trees, x, y)
    for x in range(max_x)
    for y in range(max_y)
]))
