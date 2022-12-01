from typing import List, Callable

import file_loader

input_string = file_loader.get_input()

input_string = [
    [int(x) for x in s]
    for s in input_string.splitlines()
]


def from_binary(l: List[int]) -> int:
    v = 0
    for i in l:
        if i == 0:
            v = v * 2
        else:
            v = v * 2 + 1
    return v


def most_common(l: List[int]) -> int:
    """
    returns -1 if neither 0 or 1 is most common
    """

    zeroes = 0
    ones = 0
    for i in l:
        if i == 0:
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        return 0
    if ones > zeroes:
        return 1
    return -1


def oxygen_bit_criteria(l: List[int]) -> int:
    m = most_common(l)
    if m == -1:
        return 1
    return m

def co2_bit_criteria(l: List[int]) -> int:
    m = most_common(l)
    if m == -1:
        return 0
    return (m+1)%2 # invert it


def find_value(l: List[List[int]], f: Callable[[List], int]) -> List[int]:
    if len(l) == 1:
        return l[0]
    front_digits = [i[0] for i in l]
    winning_digit = f(front_digits)
    return [winning_digit] + find_value(
        [
            i[1:] for i in l
            if i[0] == winning_digit
        ],
        f
    )

oxygen = from_binary(find_value(input_string, oxygen_bit_criteria))
co2 = from_binary(find_value(input_string, co2_bit_criteria))

print(oxygen * co2)