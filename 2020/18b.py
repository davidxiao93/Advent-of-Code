from typing import List

import file_loader

input_string = file_loader.get_input()


def evaluate(e: List[str]):
    while "(" in e:
        bl = e.index("(")
        nesting = 1
        i = bl + 1
        while nesting != 0:
            c = e[i]
            if c == "(":
                nesting += 1
            elif c == ")":
                nesting -= 1
            i += 1
        br = i - 1
        r = evaluate(e[bl+1: br])
        e = e[:bl] + [r] + e[br + 1:]

    # at this point, e has no brackets
    # evaluate all pluses
    while "+" in e:
        p = e.index("+")
        s = str(int(e[p - 1]) + int(e[p + 1]))
        e = e[:p-1] + [s] + e[p+2:]
    while "*" in e:
        p = e.index("*")
        s = str(int(e[p - 1]) * int(e[p + 1]))
        e = e[:p - 1] + [s] + e[p + 2:]
    assert(len(e) == 1)
    return e[0]

print(sum([
    int(evaluate(line.replace("(", " ( ").replace(")", " ) ").split()))
    for line in input_string.splitlines()
]))
