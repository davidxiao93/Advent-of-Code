import itertools

input = """Hit Points: 109
Damage: 8
Armor: 2"""

boss_health = int(input.splitlines()[0].split()[-1])
boss_attack = int(input.splitlines()[1].split()[-1])
boss_defend = int(input.splitlines()[2].split()[-1])

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
player wins if (k+1)*playerdamagedealt > bosshealth
              and k*bossdamagedealt < player health where k is some number of turns
(k+1) * damage(player_attack, boss_defent) > 109
k * damage(boss_attack, player_defend) < 100

k < 100 / damage(8, player_defend)
k > (109 - damage(player_attack, 2)) / damage(player_attack, 2)

(109 - damage(player_attack, 2)) / damage(player_attack, 2) < 100 / damage(8, player_defend) this one seems right?

(109 - damage(player_attack, 2)) * damage(8, player_defend) < 100 * damage(player_attack, 2) this one seems right too

"""


def player_wins(pa, pd, ph=player_health, bh=boss_health, ba=boss_attack, bd=boss_defend):
    return (bh - damage(pa, bd)) * damage(ba, pd) < ph * damage(pa, bd)

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



weapon_combinations = [[w] for w in weapons]
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

# print(all_combinations)

biggest_cost = 0
loser = []
for combo in all_combinations:
    total_cost = 0
    pa = 0
    pd = 0
    for item in combo:
        total_cost += item[1]
        pa += item[2]
        pd += item[3]

    if not player_wins(pa, pd):
        if total_cost > biggest_cost:
            biggest_cost = total_cost
            loser = combo

print(biggest_cost)
