from typing import List, Callable

import file_loader

input_string = file_loader.get_input()
num_cards = 10007


# input_string = """deal into new stack
# cut -2
# deal with increment 7
# cut 8
# cut -4
# deal with increment 7
# cut 3
# deal with increment 9
# deal with increment 3
# cut -1"""
# num_cards = 10



def deal_into_new_stack() -> Callable[[List[int]], List[int]]:
    return lambda cards: cards[::-1]

def cut_n(n: int) -> Callable[[List[int]], List[int]]:
    def cut_n_cards(cards: List[int], n: int) -> List[int]:
        n = n % len(cards)
        return cards[n:] + cards[:n]
    return lambda cards: cut_n_cards(cards, n)

def deal_with_increment_n(n: int) -> Callable[[List[int]], List[int]]:
    def deal_with_increment_n_cards(cards: List[int], n: int) -> List[int]:
        d = {}
        p = 0
        for c in cards:
            d[p] = c
            p = (p + n) % len(cards)
        return [d[p] for p in range(len(cards))]
    return lambda cards: deal_with_increment_n_cards(cards, n)

cards = [i for i in range(num_cards)]
shuffles = []
for line in input_string.splitlines():
    if "stack" in line:
        shuffles.append(deal_into_new_stack())
    elif "cut" in line:
        shuffles.append(cut_n(int(line.split()[1])))
    else:
        shuffles.append(deal_with_increment_n(int(line.split()[-1])))

for s in shuffles:
    cards = s(cards)

print(cards.index(2019))