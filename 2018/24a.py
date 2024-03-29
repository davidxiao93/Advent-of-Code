from __future__ import annotations

from typing import List, Optional, Set

import file_loader

input_string = file_loader.get_input()

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
        # returns true if this group is dead
        units_killed = attack_damage // self.hit_points_per_unit
        printd(f"{self.name()} took {attack_damage} damange, killing {units_killed} units")
        self.number_of_units -= units_killed
        return self.number_of_units <= 0

    def attack(self) -> Set[Group]:
        # returns true if enemy was killed
        if self.selected_target is None:
            printd(f"{self.name()} does not attack")
            return set()
        if self.number_of_units <= 0:
            printd(f"{self.name()} wanted to attack, but has no units")
            return set()
        enemy = self.selected_target
        self.selected_target = None
        dealt_damage = self._attack_damage_to(enemy)
        printd(f"{self.name()} attacks {enemy.name()}")
        if enemy._take_damage(dealt_damage):
            printd(f"{enemy.name()} has died")
            return { enemy }
        return set()


def battle(groups: Set[Group]) -> Set[Group]:
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
        for g in sorted(groups, key=lambda g: -1 * g.initiative):
            dead_groups |= g.attack()
        groups -= dead_groups
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


groups = set()
for army_str in input_string.split("\n\n"):
    allegience = army_str.splitlines()[0][:-1]
    groups_str = army_str.splitlines()[1:]
    for id, group_str in enumerate(groups_str):
        groups.add(parse_group(allegience, id, group_str))

groups = battle(groups)

print(sum([g.number_of_units for g in groups]))

