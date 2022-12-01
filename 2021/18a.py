from __future__ import annotations

from typing import Tuple, List, NamedTuple
import math

import file_loader

input_string = file_loader.get_input()



class RegularNumber(NamedTuple):
    value: int
    depth: int

class SnailfishNumber:
    def __init__(self, e: List[RegularNumber]):
        self.e = e

    def __add__(self, other):
        if not isinstance(other, SnailfishNumber):
            raise Exception
        new_e: List[RegularNumber] = []
        for e in self.e:
            new_e.append(RegularNumber(e.value, e.depth + 1))
        for e in other.e:
            new_e.append(RegularNumber(e.value, e.depth + 1))
        return SnailfishNumber(new_e)

    def explode(self) -> Tuple[SnailfishNumber, bool]:
        for i, e in enumerate(self.e):
            if e.depth > 4 and e.depth == self.e[i+1].depth:
                new_e: List[RegularNumber] = self.e[:i] \
                                             + [RegularNumber(0, e.depth - 1)] \
                                             + self.e[i+2:]
                left_i = i - 1
                if left_i >= 0:
                    new_e[left_i] = RegularNumber(
                        new_e[left_i].value + e.value,
                        new_e[left_i].depth
                    )
                right_i = i + 1
                if right_i < len(new_e):
                    new_e[right_i] = RegularNumber(
                        new_e[right_i].value + self.e[i+1].value,
                        new_e[right_i].depth
                    )
                return SnailfishNumber(new_e), True
        return self, False

    def split(self) -> Tuple[SnailfishNumber, bool]:
        for i, e in enumerate(self.e):
            if e.value >= 10:
                new_e: List[RegularNumber] = []
                new_e += self.e[:i]
                new_e += [RegularNumber(math.floor(e.value/2), e.depth + 1), RegularNumber(math.ceil(e.value/2), e.depth + 1)]
                new_e += self.e[i+1:]
                return SnailfishNumber(new_e), True
        return self, False

    def magnitude(self) -> int:
        magnitudes = self.e.copy()
        while len(magnitudes) > 1:
            max_depth = max([e.depth for e in magnitudes])
            for i, e in enumerate(magnitudes[:-1]):
                if e.depth == max_depth and magnitudes[i+1].depth == max_depth:
                    m = 3*e.value + 2*magnitudes[i+1].value
                    magnitudes = magnitudes[:i] \
                                + [RegularNumber(m, max_depth - 1)] \
                                + magnitudes[i+2:]
                    break
            pass

        return magnitudes[0].value


def parse_line(line: str) -> SnailfishNumber:
    depth = 0
    numbers: List[RegularNumber] = []
    for c in line:
        if c == "[":
            depth += 1
        if c == "]":
            depth -= 1
        if c.isnumeric():
            numbers.append(RegularNumber(int(c), depth))
    return SnailfishNumber(numbers)

snailfish_numbers: List[SnailfishNumber] = []
for line in input_string.splitlines():
    snailfish_numbers.append(parse_line(line))

a: SnailfishNumber = snailfish_numbers[0]
snailfish_numbers = snailfish_numbers[1:]

for s in snailfish_numbers:
    a = a + s

    while True:
        a, exploded = a.explode()
        if exploded:
            continue

        a, splitted = a.split()
        if splitted:
            continue

        break

    # a is now reduced

# a is the summed and reduced total

print(a.magnitude())


