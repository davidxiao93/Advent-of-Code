from functools import reduce
from typing import List

input = """Player 1:
28
13
25
16
38
3
14
6
29
2
47
20
35
43
30
39
21
42
50
48
23
11
34
24
41

Player 2:
27
37
9
10
17
31
19
33
40
12
32
1
18
36
49
46
26
4
45
8
15
5
44
22
7"""

def player_str_to_deck(player_str) -> List[int]:
    return [int(x) for x in player_str.splitlines()[1:]]

def play(deck0: List[int], deck1: List[int]) -> int:
    rounds = 0
    while len(deck0) != 0 and len(deck1) != 0:
        rounds += 1
        c0 = deck0.pop(0)
        c1 = deck1.pop(0)
        if c0 < c1:
            deck1.append(c1)
            deck1.append(c0)
        else:
            # making the assumption that all deck cards are unique
            deck0.append(c0)
            deck0.append(c1)
    print(rounds)
    print(deck0)
    print(deck1)
    return reduce(
        lambda a, z: a + z[0]*z[1],
        zip(
            (deck0 + deck1)[::-1],
            range(1, len(deck0 + deck1) + 1)
        ),
        0
    )


player_1_str, player_2_str = input.split("\n\n")

print(play(player_str_to_deck(player_1_str), player_str_to_deck(player_2_str)))
