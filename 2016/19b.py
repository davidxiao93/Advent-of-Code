import file_loader

input_string = file_loader.get_input()
input_value = int(input_string)

# input_value = 5

import math

elves = []

for i in range(input_value):
    elves.append((i+1, 1))

def reduce_tuple(a, b):
    return (a[0], a[1] + b[1])

def reduce(elves):
    is_odd = len(elves) % 2 == 1

    if is_odd:
        # elf at index x will steal from ((k-1)/2) + math.ceil(1.5*x) where k = total elves
        stolen_from = lambda x: int(((len(elves)-1)/2) + math.ceil(1.5 * x))
    else:
        # elf at index x will steal from (k/2) + math.floor(1.5*x) where k = total elves
        stolen_from = lambda x: int((len(elves)/2) + math.floor(1.5 * x))
    count = 0
    while stolen_from(count) < len(elves):
        # elf at index "count" steals from elf at index "stolen_from(count)"
        elves[count] = reduce_tuple(elves[count], elves[stolen_from(count)])
        elves[stolen_from(count)] = (0, 0)
        count += 1

    # shift elves so that the one at the front is the next one to do some stealing
    elves = elves[count:] + elves[:count]

    # remove elves with no presents
    new_elves = [e for e in elves if e[1] != 0]
    return new_elves

while len(elves) != 1:
    elves = reduce(elves)

print(elves[0][0])










