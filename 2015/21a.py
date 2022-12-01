import itertools

import file_loader
import math

input_string = file_loader.get_input()

boss_health = int(input_string.splitlines()[0].split()[-1])
boss_attack = int(input_string.splitlines()[1].split()[-1])
boss_defend = int(input_string.splitlines()[2].split()[-1])

player_health = 100
player_attack = 0
player_defend = 0

# boss_health = 12
# boss_attack = 7
# boss_defend = 2
#
# player_health = 8
# player_attack = 5
# player_defend = 5


def damage(attack, defend):
    return max(1, attack - defend)


"""
player wins if (k+1)*playerdamagedealt >= bosshealth
              and k*bossdamagedealt < player health where k is some number of turns
(k+1) * damage(player_attack, boss_defend) >= boss_health
k * damage(boss_attack, player_defend) < player_health

k < player_health / damage(boss_attack, player_defend)
k >= (boss_health - damage(player_attack, boss_defend)) / damage(player_attack, boss_defend)


(boss_health - damage(player_attack, boss_defend)) / damage(player_attack, boss_defend) 
<= 
some integer k
< 
player_health / damage(boss_attack, player_defend)
"""


def player_wins(pa, pd, ph=player_health, bh=boss_health, ba=boss_attack, bd=boss_defend):
    return math.ceil((bh / damage(pa, bd)) - 1) < (ph / damage(ba, pd))

weapons = {
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0)
}

armour = {
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5)
}

rings = {
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3)
}



weapon_combinations = [[]] + [[w] for w in weapons]
armour_combinations = [[]] + [[a] for a in armour]
ring_combinations = []
for q in range(0, 3):
    for subset in itertools.combinations(rings, q):
        ring_combinations.append(list(subset))

# print(weapon_combinations)
# print(armour_combinations)
# print(ring_combinations)


all_combinations = []

for w in weapon_combinations:
    for a in armour_combinations:
        for r in ring_combinations:
            all_combinations.append(w + a + r)


lowest_cost = 1000000000000
winner = []
for combo in all_combinations:
    total_cost = 0
    pa = 0
    pd = 0
    for item in combo:
        total_cost += item[1]
        pa += item[2]
        pd += item[3]

    if player_wins(pa, pd):
        if total_cost < lowest_cost:
            lowest_cost = total_cost
            winner = combo

print(winner)
print(lowest_cost)
