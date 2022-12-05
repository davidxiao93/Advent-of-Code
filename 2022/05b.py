import file_loader

input_string = file_loader.get_input()

piles = [[] for i in range(10)]
piles_string, instructions = input_string.split("\n\n")


def move(piles, num_to_move, from_id, to_id):
    moving = piles[from_id][-1*num_to_move:]
    piles[from_id] = piles[from_id][:-1 * num_to_move]
    piles[to_id] = piles[to_id] + moving
    return piles

for line in piles_string.splitlines()[:-1]:
    for i, c in enumerate(line):
        if i % 4 == 1 and c != ' ':
            pile_id = int(((i - 1)/4) + 1)
            piles[pile_id] = [c] + piles[pile_id]

for line in instructions.splitlines():
    num_to_move = int(line.split()[1])
    from_id = int(line.split()[3])
    to_id = int(line.split()[5])
    piles = move(piles, num_to_move, from_id, to_id)

print("".join([
    pile[-1]
    for pile in piles
    if len(pile) != 0
]))

