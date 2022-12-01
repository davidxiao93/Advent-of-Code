import file_loader

input_string = file_loader.get_input()

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
bottom = next(iter(in_left_not_right))


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
# bottom = "tknk" # from part a



disc_weights = {}
disc_holding = {}

for line in input_string.splitlines():
    if "->" in line:
        left, right = line.split("->", 1)
    else:
        left = line
        right = None
    name = left.split()[0].strip()
    weight = int(left.split()[1].strip()[1:-1])
    disc_weights[name] = weight
    if right is not None:
        disc_holding[name] = set()
        for r in [x.strip() for x in right.split(",")]:
            disc_holding[name].add(r)

total_disc_weights = {} # Maps program to its own weight + weight of all carried programs

def calculate_total_disc_weight(name):
    if name not in disc_holding:
        total_disc_weights[name] = disc_weights[name]
    else:
        s = 0
        for x in disc_holding[name]:
            if x not in total_disc_weights:
                calculate_total_disc_weight(x)
            s += total_disc_weights[x]
        total_disc_weights[name] = disc_weights[name] + s

calculate_total_disc_weight(bottom)

# print(total_disc_weights)

# find the unbalanced one
def find_unbalanced(name):
    if name not in disc_holding:
        return None
    holding_weights = {total_disc_weights[n] for n in disc_holding[name]}
    if len(holding_weights) == 2:
        # found unbalanced bit
        holdings = disc_holding[name]
        for held in holdings:
            result = find_unbalanced(held)
            if result is not None:
                return result
        # All higher up programs are correctly balanced so the incorrect weight must come from
        # disc_holding[name]
        for held in holdings:
            if total_disc_weights[held] != min(holding_weights):
                return disc_weights[held] + min(holding_weights) - max(holding_weights)
    else:
        return None

print(find_unbalanced(bottom))



# vmpywg
# vmpywg



