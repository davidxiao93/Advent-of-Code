from typing import Tuple, List
from functools import cmp_to_key

import file_loader
input_string = file_loader.get_input()

def compare_ints(left: int, right: int) -> int:
    if left > right:
        return -1
    if left < right:
        return 1
    return 0

# -1 for not in order, 0 for not sure, 1 for in order
def compare(left:str, right: str) -> int:
    if "," not in left and "," not in right and "[" not in left and "[" not in right:
        # both integers
        return compare_ints(int(left), int(right))
    if left.startswith("["):
        left = left[1:-1]
    if right.startswith("["):
        right = right[1:-1]
    l_parts = split(left)
    r_parts = split(right)

    for i in range(min(len(l_parts), len(r_parts))):
        c = compare(l_parts[i], r_parts[i])
        if c != 0:
            return c
    return compare_ints(len(l_parts), len(r_parts))



def split(s: str) -> List[str]:
    remaining = s
    if remaining.startswith("["):
        level = 0
        left = ""
        while level != 0 or len(left) == 0:
            c = remaining[0]
            left += c
            remaining = remaining[1:]
            if c == "[":
                level += 1
            elif c == "]":
                level -= 1
        return [left] + split(remaining[1:])
    elif "," in remaining:
        left, right = remaining.split(",", 1)
        return [left] + split(right)
    elif len(remaining) != 0:
        return [remaining]
    else:
        return []


divider_packet_1 = "[[2]]"
divider_packet_2 = "[[6]]"

packets = [
    line for line in input_string.splitlines() if len(line) != 0
] + [divider_packet_1] + [divider_packet_2]

sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
print((sorted_packets.index(divider_packet_1) + 1) * (sorted_packets.index(divider_packet_2) + 1))
