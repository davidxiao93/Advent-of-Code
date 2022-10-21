from __future__ import annotations

from typing import Tuple, List, NamedTuple
import math

input = """[[[[8,1],8],[[8,1],0]],[[8,[2,4]],[0,8]]]
[[[[2,2],[7,4]],[[9,1],6]],8]
[[[3,6],[[8,7],[2,9]]],[8,[[2,3],9]]]
[[[[4,5],[1,4]],1],[[0,8],[2,[6,8]]]]
[[7,[[4,6],[0,0]]],[[4,3],5]]
[[[[8,4],4],[[4,4],[1,0]]],[[5,[5,5]],[[5,2],1]]]
[[[0,[5,8]],[1,7]],[[[5,0],[1,3]],7]]
[4,[[[6,2],[7,8]],[0,[4,4]]]]
[[[3,[5,3]],8],[[[6,8],4],[8,9]]]
[[[6,0],[9,[8,1]]],[[[9,7],3],0]]
[[9,[[9,3],[0,8]]],[[[5,3],0],[[5,6],2]]]
[[3,[[7,7],3]],[[7,[5,2]],[[6,9],0]]]
[1,[4,[3,8]]]
[[[[0,2],9],[[0,7],8]],[[5,4],[2,8]]]
[[[[1,8],9],[1,7]],[[4,[8,5]],[[6,3],[1,0]]]]
[[9,[[4,3],[3,3]]],[[[4,9],[0,9]],6]]
[7,[[8,0],[5,6]]]
[[[[3,2],1],[[4,9],6]],[[9,[1,1]],[[8,7],1]]]
[[[[5,1],[3,3]],0],[1,[[3,2],2]]]
[[7,9],[[9,9],[5,[9,5]]]]
[[[[4,3],[1,7]],[4,[9,2]]],[[6,[1,7]],[[8,0],3]]]
[[[5,[2,8]],[[1,2],7]],[[3,[0,5]],[[3,5],8]]]
[[[[2,2],6],[[2,1],7]],[[[4,6],8],7]]
[[2,[[3,0],[0,5]]],[[[3,4],[0,1]],0]]
[[[[9,9],5],[[9,9],6]],[[[4,1],2],0]]
[4,[[2,9],[6,2]]]
[[[8,6],6],7]
[[7,[8,2]],[[[5,5],6],[9,0]]]
[5,[[2,5],[[4,9],[8,6]]]]
[[4,[7,[9,6]]],7]
[[[9,[3,3]],[[3,1],[8,7]]],[[6,[3,5]],[4,1]]]
[[8,6],[8,[[0,2],[8,1]]]]
[6,[8,[[7,7],0]]]
[3,4]
[[9,[8,0]],[[[7,8],3],1]]
[5,[[3,[8,7]],[[5,0],[9,7]]]]
[[[[4,2],9],[6,[0,2]]],6]
[[4,[3,[4,9]]],[[4,[1,6]],1]]
[[[6,3],[8,8]],[5,[[9,3],[6,3]]]]
[[[9,9],[[7,1],6]],[[[1,0],[7,4]],[3,[2,0]]]]
[[[[2,5],9],[3,[6,2]]],[4,7]]
[[1,[7,8]],[[[0,1],8],[[1,1],9]]]
[[[9,[6,4]],[[9,8],[0,2]]],[[[8,9],[2,3]],[3,[8,0]]]]
[[[[6,8],2],3],[[2,2],5]]
[[[4,[8,5]],[[4,3],1]],[[[2,4],[4,4]],[[4,1],[1,7]]]]
[[[[2,6],6],[[9,2],4]],[[[9,9],[9,5]],5]]
[[[[7,5],[4,9]],4],[[[0,7],[3,6]],[[6,5],[3,0]]]]
[[[4,4],[[5,7],[8,5]]],[0,8]]
[[3,[[1,3],[7,5]]],[6,[[8,1],0]]]
[[[9,9],[5,[9,6]]],[[[4,0],[5,4]],6]]
[0,[[[9,2],4],3]]
[[[1,[8,5]],[0,[6,0]]],[[[6,5],[3,1]],[[6,2],[1,5]]]]
[[[4,0],[4,7]],6]
[1,[[[5,2],9],[[3,9],4]]]
[[[[9,6],[4,1]],4],[2,[[0,2],6]]]
[9,[[[1,5],[3,1]],1]]
[5,0]
[9,[[[7,5],[2,1]],[[2,3],[5,3]]]]
[[5,[[0,5],[9,5]]],[[[2,7],3],[[2,9],[3,5]]]]
[[[1,9],2],[[7,[1,7]],[8,[9,8]]]]
[[8,9],[[5,[9,0]],[[6,8],[5,2]]]]
[6,[[[1,3],[0,8]],4]]
[[[[9,8],[0,9]],[[8,4],[3,5]]],[[[5,0],8],[[6,8],1]]]
[[6,[[1,4],[7,0]]],[[3,4],[[2,1],[2,7]]]]
[[[5,0],[3,[4,7]]],[[9,3],[[9,4],[9,6]]]]
[[[[8,3],[8,0]],5],[[[5,5],[0,2]],[[0,1],9]]]
[[[[6,4],[1,8]],[3,[0,2]]],[8,[[8,8],5]]]
[2,[[2,1],[1,4]]]
[8,[0,[3,5]]]
[[[[0,2],3],[[4,9],[1,2]]],[[8,2],[6,[7,1]]]]
[[[0,0],9],1]
[8,[[4,1],[[1,3],9]]]
[[[8,[5,9]],9],[[[5,7],[9,0]],3]]
[[5,[2,9]],7]
[5,6]
[[[[7,5],[8,3]],[[4,3],8]],[[2,2],[[7,2],[4,2]]]]
[[[9,5],[3,[1,5]]],6]
[[[[7,4],[7,9]],[[3,1],[3,1]]],[[[6,4],[0,1]],1]]
[[3,[[7,4],9]],[[[5,8],[2,7]],[[0,4],[3,6]]]]
[[[3,[2,3]],[[6,0],[7,7]]],1]
[[2,[[8,8],[2,3]]],[5,2]]
[[[0,[5,5]],[8,1]],5]
[[3,9],[6,[[0,5],[1,7]]]]
[[[[3,0],9],[8,2]],[[[2,2],8],0]]
[[[9,6],[[5,1],[4,9]]],[[[1,1],[0,3]],[[4,9],[7,5]]]]
[[[2,[6,1]],[[5,7],[9,2]]],[[[4,2],8],9]]
[[9,[7,1]],[[4,5],[9,1]]]
[[9,[5,0]],[[1,7],[[9,6],[4,5]]]]
[[[[1,1],[8,7]],4],[[0,4],[[1,7],[3,5]]]]
[[5,[1,[8,4]]],[[[9,4],0],[1,[5,5]]]]
[[[5,[1,6]],[6,0]],[[0,[9,7]],1]]
[2,[9,[[0,3],[2,3]]]]
[3,[4,[[0,9],8]]]
[[5,6],[[[9,9],[4,0]],[7,[2,0]]]]
[[[[5,1],6],[[1,0],[7,1]]],[[6,[1,0]],[[4,2],[0,0]]]]
[[[4,[0,2]],6],[[[4,3],[8,0]],[[9,6],[1,5]]]]
[[[[5,3],[2,2]],[8,[8,3]]],[[9,1],2]]
[[3,4],[[[4,7],[2,3]],[9,[9,0]]]]
[[[5,[6,2]],[[1,5],[9,2]]],[[[7,9],3],[[6,7],[6,2]]]]
[[[5,3],9],[[2,[4,3]],[[5,3],1]]]"""



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
for line in input.splitlines():
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


