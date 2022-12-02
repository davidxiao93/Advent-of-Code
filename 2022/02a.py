import file_loader

input_string = file_loader.get_input()

from enum import Enum

class Action(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


play = {
    "A": Action.ROCK,
    "B": Action.PAPER,
    "C": Action.SCISSORS,

    "X": Action.ROCK,
    "Y": Action.PAPER,
    "Z": Action.SCISSORS
}

def winner(other: Action, player: Action) -> int:
    if other == player:
        return 0
    if (other.value + 1) % 3 == player.value:
        return 1 # player wins
    return -1

def score_game(other: Action, player: Action) -> int:
    return player.value + 1 + 3 * (winner(other, player) + 1)


total = 0
for line in input_string.splitlines():
    o, p = line.split()
    total += score_game(play[o], play[p])

print(total)