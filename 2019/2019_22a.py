from typing import List, Callable

input = """deal with increment 65
deal into new stack
deal with increment 25
cut -6735
deal with increment 3
cut 8032
deal with increment 71
cut -4990
deal with increment 66
deal into new stack
cut -8040
deal into new stack
deal with increment 18
cut -8746
deal with increment 42
deal into new stack
deal with increment 17
cut -8840
deal with increment 55
cut -4613
deal with increment 10
cut -5301
deal into new stack
deal with increment 21
cut -5653
deal with increment 2
cut 5364
deal with increment 72
cut -3468
deal into new stack
cut -9661
deal with increment 63
cut 6794
deal with increment 43
cut 2935
deal with increment 66
cut -1700
deal with increment 6
cut 5642
deal with increment 64
deal into new stack
cut -5699
deal with increment 43
cut -9366
deal with increment 42
deal into new stack
cut 2364
deal with increment 13
cut 8080
deal with increment 2
deal into new stack
cut -9602
deal with increment 51
cut 3214
deal into new stack
cut -2995
deal with increment 57
cut -8169
deal into new stack
cut 362
deal with increment 41
cut -4547
deal with increment 56
cut -1815
deal into new stack
cut 1554
deal with increment 71
cut 2884
deal with increment 44
cut -2423
deal with increment 4
deal into new stack
deal with increment 20
cut -2242
deal with increment 48
cut -716
deal with increment 29
cut -6751
deal with increment 45
cut -9511
deal with increment 75
cut -440
deal with increment 35
cut 6861
deal with increment 52
cut -4702
deal into new stack
deal with increment 28
cut 305
deal with increment 16
cut 7094
deal into new stack
cut 5175
deal with increment 30
deal into new stack
deal with increment 61
cut 1831
deal into new stack
deal with increment 25
cut 4043"""
num_cards = 10007


# input = """deal into new stack
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
for line in input.splitlines():
    if "stack" in line:
        shuffles.append(deal_into_new_stack())
    elif "cut" in line:
        shuffles.append(cut_n(int(line.split()[1])))
    else:
        shuffles.append(deal_with_increment_n(int(line.split()[-1])))

for s in shuffles:
    cards = s(cards)

print(cards.index(2019))