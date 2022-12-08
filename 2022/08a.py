from typing import List, Tuple

import file_loader

input_string = file_loader.get_input()

trees = [
    [
        (int(c), False) for c in line
    ] for line in input_string.splitlines()
]

def rotate_trees(trees: List[List[Tuple[int, bool]]]) -> List[List[Tuple[int, bool]]]:
    new_lines = [[] for i in range(len(trees[0]))]
    for line in trees:
        for i, c in enumerate(line):
            new_lines[i] = [c] + new_lines[i]
    return new_lines

def check_line_visibility(trees: List[Tuple[int, bool]]) -> List[Tuple[int, bool]]:
    height = -1
    visible_trees = []
    for tree in trees:
        if tree[0] > height:
            height = tree[0]
            visible_trees.append((tree[0], True))
        else:
            visible_trees.append(tree)
    return visible_trees

def check_visibility(trees :List[List[Tuple[int, bool]]]) -> List[List[Tuple[int, bool]]]:
    new_visible_trees = []
    for tree_line in trees:
        new_visible_trees.append(check_line_visibility(tree_line))
    return new_visible_trees


for i in range(4):
    trees = check_visibility(trees)
    trees = rotate_trees(trees)

total_visible = 0
for tree_line in trees:
    for tree in tree_line:
        if tree[1]:
            total_visible += 1

print(total_visible)
