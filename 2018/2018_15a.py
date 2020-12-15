from __future__ import annotations
from typing import List, Set, Optional

input = """################################
###########################..###
##########################...###
#########################..#####
####...##################.######
#####..################...#.####
#..G...G#########.####G.....####
#.......########.....G.......###
#.....G....###G....#....E.....##
####...##......##.............##
####G...#.G...###.G...........##
####G.......................####
####.........G#####.........####
####...GG#...#######.......#####
###.........#########G....######
###.G.......#########G...#######
###.G.......#########......#####
####.....G..#########....E..####
#####.......#########..E....####
######...##G.#######........####
######.#.#.G..#####.....##..####
########....E...........##..####
########....E#######........####
########......######E....##..E.#
########......#####.....#......#
########.....######............#
##################...#.E...E...#
##################.............#
###################.......E#####
####################....#...####
####################.###########
################################"""


# # example 0
# input = """#######
# #.G...#
# #...EG#
# #.#.#G#
# #..G#E#
# #.....#
# #######"""
#
# # example 1
# input = """#######
# #G..#E#
# #E#E.E#
# #G.##.#
# #...#E#
# #...E.#
# #######"""
#
# # example 2
# input = """#######
# #E..EG#
# #.#G.E#
# #E.##E#
# #G..#.#
# #..E#.#
# #######"""
#
# # example 3
# input = """#######
# #E.G#.#
# #.#G..#
# #G.#.G#
# #G..#.#
# #...E.#
# #######"""
#
# # example 4
# input = """#######
# #.E...#
# #.#..G#
# #.###.#
# #E#G#G#
# #...#G#
# #######"""
#
# # example 5
# input = """#########
# #G......#
# #.E.#...#
# #..##..G#
# #...##..#
# #...#...#
# #.G...G.#
# #.....G.#
# #########"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x = 0, y = -1)
down = Point(x = 0, y = 1)
left = Point(x = -1, y = 0)
right = Point(x = 1, y = 0)
directions = [up, left, right, down] # reading order!

def add_point(p: Point, q: Point):
    return Point(x = p.x + q.x, y = p.y + q.y)


def pop_next(dict):
    min_key = min(dict)
    set_value = dict[min_key]
    return_value = set_value.pop()
    if len(set_value) == 0:
        dict.pop(min_key, None)
    return return_value, min_key


def dijkstra(start: Point, ends: Set[Point], obstacles: Set[Point]) -> Optional[Point]:
    # Returns the point in end that is nearest to the start
    step_mapping = {
        0: {start}
    }
    visited_points = set()
    shortest = None
    nearest_targets = set()
    while True:
        if len(step_mapping) == 0:
            break
        p, steps = pop_next(step_mapping)
        if shortest is not None:
            if steps > shortest:
                break
            elif steps == shortest and p in ends:
                nearest_targets.add(p)
        if p in ends and shortest is None:
            shortest = steps
            nearest_targets.add(p)
        visited_points.add(p)
        for d in directions:
            neighbour = add_point(p, d)
            if neighbour in obstacles or neighbour in visited_points:
                continue
            if steps + 1 not in step_mapping:
                step_mapping[steps + 1] = set()
            step_mapping[steps + 1].add(neighbour)
    if len(nearest_targets) == 0:
        return None
    return sorted(nearest_targets, key=lambda point: (point.y, point.x))[0]


class Unit:
    def __init__(self, position, allegiance, units: Set[Unit], walls: Set[Point]):
        self.position = position
        self.allegiance = allegiance
        self.health = 200
        self.attack_power = 3
        self.units = units
        self.walls = walls

    def is_battle_over(self) -> bool:
        return len([unit for unit in self.units if unit.allegiance != self.allegiance]) == 0

    def is_in_range(self) -> Optional[Unit]:
        # returns unit to attack if it is in range
        # else returns None
        attack_candidates = []
        for d in directions:
            candidate = add_point(self.position, d)
            if candidate in self.walls:
                # cant target walls
                continue
            for unit in self.units:
                if unit == self:
                    # ignore self
                    continue
                if unit.allegiance == self.allegiance:
                    # ignore friendlies
                    continue
                if unit.position == candidate:
                    attack_candidates.append(unit)
                    break
        if len(attack_candidates) == 0:
            return None
        lowest_health = min(attack_candidates, key=lambda enemy: enemy.health).health
        return sorted(
            [enemy for enemy in attack_candidates if enemy.health == lowest_health],
            key=lambda enemy: (enemy.position.y, enemy.position.x)
        )[0]

    def attack(self, enemy: Unit) -> bool:
        # returns True if enemy is killed
        # False otherwise
        enemy.health -= self.attack_power
        return enemy.health <= 0

    def next_step(self, target: Point, taken_positions: Set[Point]) -> Optional[Point]:
        # returns the position to move next towards target
        return dijkstra(target, {add_point(self.position, d) for d in directions}, taken_positions)


    def pick_next(self, in_range_positions: Set[Point], taken_positions: Set[Point]) -> Optional[Point]:
        # returns the target position
        return dijkstra(self.position, in_range_positions, taken_positions)


    def move(self):
        taken_positions = self.walls | {unit.position for unit in self.units}
        enemies = {unit for unit in self.units if unit.allegiance != self.allegiance}
        in_range_positions = set()
        for enemy in enemies:
            for d in directions:
                candidate_point = add_point(enemy.position, d)
                if candidate_point not in taken_positions:
                    in_range_positions.add(candidate_point)
        target = self.pick_next(in_range_positions, taken_positions)
        if target is not None:
            next_position = self.next_step(target, taken_positions)
            if next_position is not None:
                self.position = next_position


    def take_turn(self) -> bool:
        # returns False if battle not over, True if battle is over
        if self.health <= 0:
            # prevent units taking a turn when they are dead
            return False
        battle_over = self.is_battle_over()
        if battle_over:
            return True
        enemy = self.is_in_range()
        if enemy is None:
            self.move()
            enemy = self.is_in_range()
        if enemy is not None:
            enemy_death = self.attack(enemy)
            if enemy_death:
                self.units.remove(enemy)
        return False


walls = set()
units = set()

for y, line in enumerate(input.splitlines()):
    for x, c in enumerate(line):
        if c == "#":
            walls.add(Point(x, y))
        elif c == "G" or c == "E":
            units.add(Unit(Point(x, y), c, units, walls))


def pretty_print(units, walls):
    unit_dict = {
        unit.position: (unit.allegiance, unit.health)
        for unit in units
    }
    for y, line in enumerate(input.splitlines()):
        row = []
        healths = []
        for x in range(len(line)):
            p = Point(x, y)
            if p in walls:
                row.append("#")
            elif p in unit_dict:
                row.append(unit_dict[p][0])
                healths.append(unit_dict[p][0] + "(" + str(unit_dict[p][1]) + ")")
            else:
                row.append(".")
        print("".join(row) + "    " + ", ".join(healths))

rounds = 0
while True:
    for unit in sorted(units, key=lambda unit: (unit.position.y, unit.position.x)):
        battle_over = unit.take_turn()
        if battle_over:
            print(rounds * sum([unit.health for unit in units]))
            # pretty_print(units, walls)
            exit(0)
    # pretty_print(units, walls)
    rounds += 1





