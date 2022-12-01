from typing import List

import file_loader

input_string = file_loader.get_input()

"""
board positions
0  1  2  3  4 
5  6  7  8  9 
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
"""

drawn_values = [int(x) for x in input_string.splitlines()[0].split(",")]
input_string = input_string.splitlines()[2:]



wins = []
for i in range(5):
    wins.append(set([5*s + i for s in range(5)]))
    wins.append(set([5*i + s for s in range(5)]))


class Board:
    def __init__(self, values: List[List[int]]):
        self.pos = dict() # maps board value to position
        self.sum_of_all_values_on_board = 0
        for y, line in enumerate(values):
            for x, v in enumerate(line):
                self.pos[v] = 5*y + x
                self.sum_of_all_values_on_board += v
        self.drawn_positions = set()
        self.sum_of_drawn_values_on_board = 0

    def call(self, drawn: int):
        self.last_drawn = drawn
        if drawn in self.pos:
            self.drawn_positions.add(self.pos[drawn])
            self.sum_of_drawn_values_on_board += drawn

    def is_win(self) -> int:
        """
        returns -1 if not win, otherwise the score
        """
        for w in wins:
            if w.issubset(self.drawn_positions):
                return (self.sum_of_all_values_on_board - self.sum_of_drawn_values_on_board) * self.last_drawn
        return -1

boards = []

for i in range(0, len(input_string), 6):
    boards.append(Board([[int(x) for x in input_string[i + j].split()] for j in range(5)]))

last_drawn_pos = -1
last_win = -1
for b in boards:
    for i, v in enumerate(drawn_values):
        b.call(v)
        score = b.is_win()
        if score != -1:
            if last_drawn_pos < i:
                last_drawn_pos = i
                last_win = score
            break

print(last_win)