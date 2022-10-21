from collections import namedtuple
from typing import Optional

input = """Hit Points: 58
Damage: 9"""

"""
Note from future David:
Be warned that this one can take time. It takes 5 minutes on my laptop.
"""

boss_health = int(input.splitlines()[0].split()[-1])
boss_attack =int(input.splitlines()[1].split()[-1])

player_health = 50
player_mana = 500
player_attack = 0
player_defence = 0




# boss_health = 14
# boss_attack = 8
#
# player_health = 10
# player_mana = 250

is_debug_state = False

def damage(attack, defend):
    return max(1, attack - defend)

class LoseException(Exception):
    pass

class WinException(Exception):
    # Yes i know this is disgusting but i cba to do something better
    pass

def printd(*args):
    if is_debug_state:
        print(*args)

class Player:
    def __init__(self):
        self.starting_health = player_health
        self.health = self.starting_health
        self.mana = player_mana
        self.attack = player_attack
        self.defence = player_defence

    def set_defence(self, defence):
        self.defence = defence

    def add_mana(self, delta):
        self.mana += delta

    def add_health(self, delta):
        self.health += delta
        if self.health > self.starting_health:
            self.health = self.starting_health
        if self.health <= 0:
            raise LoseException("Out of health")

class Boss:
    def __init__(self):
        self.health = boss_health
        self.attack = boss_attack

    def add_health(self, delta):
        self.health += delta
        if self.health <= 0:
            raise WinException()

Players = namedtuple("Players", ["player", "boss"])

Effect = namedtuple("Effect", ["name", "turn_effect", "end_effect", "timer"])

class Effects:
    def __init__(self):
        self.name_to_effect = {}
        self.name_to_timer = {}

    def apply_effects(self, players: Players):
        effects_to_remove = []
        for name in self.name_to_effect.keys():
            self.name_to_timer[name] -= 1
            printd(self.name_to_effect[name].name.title(), "was applied, timer is", self.name_to_timer[name])
            self.name_to_effect[name].turn_effect(players)
            if self.name_to_timer[name] <= 0:
                if self.name_to_effect[name].end_effect is not None:
                    self.name_to_effect[name].end_effect(players)
                effects_to_remove.append(name)
        for name in effects_to_remove:
            self.name_to_timer.pop(name, None)
            self.name_to_effect.pop(name, None)

    def add_effect(self, effect: Effect):
        if effect is None:
            return
        if effect.name in self.name_to_effect or effect.name in self.name_to_timer:
            raise LoseException("Invalid combo")
        self.name_to_timer[effect.name] = effect.timer
        self.name_to_effect[effect.name] = effect

    def pretty_print(self):
        if len(self.name_to_timer) > 0:
            printd("Effects:")
        for name, timer in self.name_to_timer.items():
            printd(name, "with", timer, "turns remaining")


class Spell:
    def __init__(self, name, mana_use, immediate_effect, repeated_effect: Optional[Effect] ):
        self.name = name
        self.mana_use = mana_use
        self.immediate_effect = immediate_effect
        self.repeated_effect = repeated_effect

    def apply_spell(self, players: Players, effects: Effects):
        if players.player.mana < self.mana_use:
            raise LoseException("Out of Mana")
        players.player.add_mana(-1 * self.mana_use)
        if self.immediate_effect is not None:
            self.immediate_effect(players)
        effects.add_effect(self.repeated_effect)


def drain_method(players: Players):
    players.player.add_health(2)
    players.boss.add_health(-2)


magic_missile = Spell(
    "Magic Missile",
    53,
    lambda players: players.boss.add_health(-4),
    None
)

drain = Spell(
    "Drain",
    73,
    lambda players: drain_method(players),
    None
)

shield = Spell(
    "Shield",
    113,
    None,
    Effect("shield",
           lambda players: players.player.set_defence(7),
           lambda players: players.player.set_defence(0),
           6)
)

poison = Spell(
    "Poison",
    173,
    None,
    Effect("poison",
           lambda players: players.boss.add_health(-3),
           None,
           6)
)

recharge = Spell(
    "Recharge",
    229,
    None,
    Effect("recharge",
           lambda players: players.player.add_mana(101),
           None,
           5)
)

def boss_attack_method(players: Players):
    players.player.add_health(-1 * damage(players.boss.attack, players.player.defence))


def score_spells(spells):
    total = 0
    for spell in spells:
        total += spell.mana_use
    return total

class State:
    def __init__(self):
        self.players = Players(Player(), Boss())
        self.effects = Effects()
        self.spells_applied = []
        self.next_spell = None

    def set_next_move(self, spell: Spell):
        self.next_spell = spell

    def apply_next_move(self):
        if self.next_spell is None:
            return

        ## hard mode bit starts
        self.players.player.add_health(-1)
        ## hard mode bit ends
        self.player_move(self.next_spell)
        self.boss_move()
        self.next_spell = None

    def player_move(self, spell: Spell):
        printd("-- Player Turn --")
        self.__pretty_print()
        self.effects.apply_effects(self.players)
        printd("Player casts", spell.name)
        self.spells_applied.append(spell)
        spell.apply_spell(self.players, self.effects)
        printd("")

    def boss_move(self):
        printd("-- Boss Turn --")
        self.__pretty_print()
        self.effects.apply_effects(self.players)
        printd("Boss attacks")
        boss_attack_method(self.players)
        printd("")

    def get_score(self):
        val = score_spells(self.spells_applied)
        if self.next_spell is not None:
            val += self.next_spell.mana_use
        return val

    def get_spell_names(self):
        return [spell.name for spell in self.spells_applied]

    def __pretty_print(self):
        printd("- Player has",
              self.players.player.health, "hit points,",
              self.players.player.defence, "armour,",
              self.players.player.mana, "mana"
              )
        printd("- Boss has",
              self.players.boss.health, "hit points")





# import cProfile
# pr = cProfile.Profile()
# pr.enable()

from copy import deepcopy


c = {
    0: [State()]
}

def pop_next(c):
    min_key = min(c)
    states = c[min_key]
    return_value = states[0]
    states.pop(0)
    if len(states) == 0:
        c.pop(min_key, None)
    return return_value

def add_next(c, key, value):
    if key not in c:
        c[key] = []
    c[key].append(value)

import time
start = time.time()
is_found = None

counter = 0

while not is_found:
    counter += 1
    next_candidate = pop_next(c)
    try:
        next_candidate.apply_next_move()
    except LoseException:
        continue
    except WinException:
        is_found = next_candidate
        # print("Winning Combo:", ", ".join([spell.name for spell in is_found.spells_applied]))
        print(score_spells(is_found.spells_applied))
        # end = time.time()
        # print(end - start)
        exit(0)

    # if counter % 500 == 0:
    #     print("Checked:", ", ".join(next_candidate.get_spell_names()))
    #     print("This scored:", next_candidate.get_score())
    #     print("time taken", time.time() - start)
    #     print("")

    # battle not over yet!
    for spell in [magic_missile, drain]:
        s = deepcopy(next_candidate)
        s.set_next_move(spell)
        add_next(c, s.get_score(), s)
    for spell in [shield, poison, recharge]:
        if len(next_candidate.spells_applied) >= 2 \
                and (next_candidate.spells_applied[-1] == spell
                    or next_candidate.spells_applied[-2] == spell):
            continue
        s = deepcopy(next_candidate)
        s.set_next_move(spell)
        add_next(c, s.get_score(), s)


#
# pr.disable()
# pr.print_stats(sort="calls")


print("oh dear")

exit()

