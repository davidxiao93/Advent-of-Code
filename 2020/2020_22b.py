from functools import reduce
from typing import List

input = """Player 1:
3
42
4
25
14
36
32
18
33
10
35
50
16
31
34
46
9
6
41
7
15
45
30
27
49

Player 2:
8
11
47
21
17
39
29
43
23
28
13
22
5
20
44
38
26
37
2
24
48
12
19
1
40"""

def player_str_to_deck(player_str) -> List[int]:
    return [int(x) for x in player_str.splitlines()[1:]]




def play_round(player_1: List[int], seen_for_player_1, player_2: List[int], seen_for_player_2) -> int:
    player_1_deck = ",".join([str(x) for x in player_1])
    # print("P1:", player_1_deck)
    if player_1_deck in seen_for_player_1:
        return -1
    seen_for_player_1.add(player_1_deck)
    player_2_deck = ",".join([str(x) for x in player_2])
    # print("P2:", player_2_deck)
    if player_2_deck in seen_for_player_2:
        return -1
    seen_for_player_2.add(player_2_deck)

    c1 = player_1.pop(0)
    # print("P1 plays", c1)
    c2 = player_2.pop(0)
    # print("P2 plays", c2)

    if c1 > len(player_1) or c2 > len(player_2):
        if c1 < c2:
            # print("P2 wins by high card")
            player_2.append(c2)
            player_2.append(c1)
            return 2
        else:
            # print("P1 wins by high card")
            player_1.append(c1)
            player_1.append(c2)
            return 1

    # print("Recursing")
    winner = play((player_1.copy())[:c1], list(player_2.copy())[:c2])
    # print("Finished Recursing")
    if winner == 1:
        # print("P1 wins by recursion")
        player_1.append(c1)
        player_1.append(c2)
        return 1
    else:
        # print("P2 wins by recursion")
        player_2.append(c2)
        player_2.append(c1)
        return 2


def play(player_1: List[int], player_2: List[int]) -> int:
    round_winner = 0
    seen_for_player_1 = set()
    seen_for_player_2 = set()
    while len(player_1) != 0 and len(player_2) != 0:
        round_winner = play_round(player_1, seen_for_player_1, player_2, seen_for_player_2)
        if round_winner == -1:
            round_winner = 1
            break
    # print(f"P{round_winner} wins game")
    return round_winner

player_1_str, player_2_str = input.split("\n\n")

player_1 = player_str_to_deck(player_1_str)
player_2 = player_str_to_deck(player_2_str)

winner = play(player_1, player_2)
winning_deck = player_1 if winner == 1 else player_2

print(reduce(
        lambda a, z: a + z[0]*z[1],
        zip(
            winning_deck[::-1],
            range(1, len(winning_deck) + 1)
        ),
        0
    ))
