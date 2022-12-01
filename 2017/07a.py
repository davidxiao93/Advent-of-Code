import file_loader

input_string = file_loader.get_input()

# input_string = """pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)"""



# The program on the bottom is the only one on the left side of the arrow that doesnt appear on the right

left_side = set()
right_side = set()

for line in input_string.splitlines():
    if "->" in line:
        left, right = line.split("->", 1)
        for r in [x.strip() for x in right.split(",")]:
            right_side.add(r)
    else:
        left = line
    left_side.add(left.split()[0].strip())

in_left_not_right = left_side - right_side
print(next(iter(in_left_not_right)))