from __future__ import annotations

from typing import List, Optional, Set

import file_loader

input_string = file_loader.get_input()

# input_string = """Immune System:
# 17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
# 989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3
#
# Infection:
# 801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
# 4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

def printd(message):
    # print(message)
    pass

class Group:
    def __init__(self,
                 allegience: str,
                 id: int,
                 num_units: int,
                 hit_points_per_unit: int,
                 attack_per_unit: int,
                 attack_type: str,
                 initiative: int,
                 weaknesses: List[str] = None,
                 immunities: List[str] = None):
        self.allegience = allegience
        self.id = id
        self.number_of_units = num_units
        self.hit_points_per_unit = hit_points_per_unit
        self.attack_per_unit = attack_per_unit
        self.attack_type = attack_type
        self.initiative = initiative
        self.weaknesses = [] if weaknesses is None else weaknesses
        self.immunities = [] if immunities is None else immunities

        self.selected_target: Optional[Group] = None

    def name(self):
        return f"{self.allegience} group {self.id}"

    def effective_power(self) -> int:
        return self.number_of_units * self.attack_per_unit

    def _attack_damage_to(self, enemy: Group) -> int:
        if self.attack_type in enemy.immunities:
            return 0
        if self.attack_type in enemy.weaknesses:
            return self.effective_power() * 2
        return self.effective_power()

    def choose_target_group(self, remaining_groups: Set[Group]) -> Optional[Group]:
        enemy_groups = [g for g in remaining_groups if g.allegience != self.allegience]
        if len(enemy_groups) == 0:
            printd(f"{self.name()} has choosen to not attack")
            self.selected_target = None
        else:
            best_target = max(
                enemy_groups,
                key=lambda g: (self._attack_damage_to(g), g.effective_power(), g.initiative)
            )
            if self._attack_damage_to(best_target) == 0:
                # cannot do any damage to any enemy
                self.selected_target = None
                printd(f"{self.name()} has choosen to not attack")
            else:
                self.selected_target = best_target
                printd(f"{self.name()} has choosen to attack {self.selected_target.name()}")
        return self.selected_target

    def _take_damage(self, attack_damage: int) -> bool:
        # returns true if some units were killed
        units_killed = attack_damage // self.hit_points_per_unit
        printd(f"{self.name()} took {attack_damage} damange, killing {units_killed} units")
        self.number_of_units -= units_killed
        return units_killed > 0

    def attack(self) -> bool:
        # returns true if some enemy units were killed
        if self.selected_target is None:
            printd(f"{self.name()} does not attack")
            return False
        if self.number_of_units <= 0:
            printd(f"{self.name()} wanted to attack, but has no units")
            return False
        enemy = self.selected_target
        self.selected_target = None
        dealt_damage = self._attack_damage_to(enemy)
        printd(f"{self.name()} attacks {enemy.name()}")
        return enemy._take_damage(dealt_damage)


def battle(groups: Set[Group], boost: int) -> Set[Group]:

    for g in groups:
        if g.allegience == "Immune System":
            g.attack_per_unit += boost

    while len({g.allegience for g in groups}) != 1:

        printd("Status:")
        for g in sorted(groups, key=lambda g: (g.allegience, g.id)):
            printd(f"{g.name()} has {g.number_of_units} units")

        printd("")
        printd("Target selection")
        targetted_groups = set()
        for g in sorted(groups, key=lambda g: (-1 * g.effective_power(), -1 * g.initiative)):
            target = g.choose_target_group(groups - targetted_groups)
            targetted_groups.add(target)


        printd("")
        printd("Attacking phase")
        dead_groups = set()
        units_killed = False
        for g in sorted(groups, key=lambda g: -1 * g.initiative):
            units_killed = g.attack() or units_killed

        # remove dead groups
        for g in groups:
            if g.number_of_units <= 0:
                printd(f"{g.name()} has died")
                dead_groups.add(g)
        groups -= dead_groups

        if not units_killed:
            # stalemate
            break
        printd("")
    return groups


def parse_group(allegience: str, id: int, string: str) -> Group:
    words = string.split()
    num_units = int(words[0])
    hit_points = int(words[4])
    initiative = int(words[-1])
    attack_type = words[-5]
    attack_damage = int(words[-6])
    weaknesses = []
    immunities = []
    if "(" in string:
        bracketed = string.split("(")[1].split(")")[0].split(";")
        for b in bracketed:
            attack_types = [x.strip().replace(",", "") for x in b.split()[2:]]
            if "immune" in b:
                immunities += attack_types
            elif "weak" in b:
                weaknesses += attack_types
            else:
                print("Cannot parse")
                exit(1)
    return Group(allegience,
                 id + 1,
                 num_units,
                 hit_points,
                 attack_damage,
                 attack_type,
                 initiative,
                 weaknesses,
                 immunities)

def parse_input(input_str: str) -> Set[Group]:
    groups = set()
    for army_str in input_str.split("\n\n"):
        allegience = army_str.splitlines()[0][:-1]
        groups_str = army_str.splitlines()[1:]
        for id, group_str in enumerate(groups_str):
            groups.add(parse_group(allegience, id, group_str))
    return groups

boost = 0
while True:
    winner = battle(parse_input(input_string), boost)
    resulting_alligiences = {g.allegience for g in winner}
    if "Immune System" in resulting_alligiences and len(resulting_alligiences) == 1:
        print(sum([g.number_of_units for g in winner]))
        break
    boost += 1



