from typing import List
import file_loader

input_string = file_loader.get_input()
cups = [int(x) for x in input_string]

def do_round(cups: List[int]) -> List[int]:
    # current cup is always at the front
    current_cup = cups[0]
    moved_cups = cups[1:4]
    found = 0
    find_value = current_cup - 1
    if find_value < min(cups):
        find_value = max(cups)
    while not found:
        new_index = cups.index(find_value)
        if new_index >= 4:
            found = new_index
        else:
            find_value -= 1
            if find_value < min(cups):
                find_value = max(cups)
    return cups[4: found+1] + moved_cups + cups[found + 1:] + [cups[0]]


for i in range(100):
    cups = do_round(cups)

one_index = cups.index(1)
print("".join([str(x) for x in cups[one_index+1:] + cups[:one_index]]))
