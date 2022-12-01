import file_loader

input_string = file_loader.get_input()
input_value = int(input_string)

# input_string = 5

elves = []

for i in range(input_value):
    elves.append((i+1, 1))

def reduce_tuple(es):
    if len(es) == 1:
        return es[0]
    return (es[0][0], es[0][1] + es[1][1])

def reduce(elves):
    is_odd = len(elves) % 2 == 1
    elves = [reduce_tuple(elves[i:i + 2]) for i in range(0, len(elves), 2)]
    if is_odd:
        elves = elves[-1:] + elves[:-1]
    return elves

while len(elves) != 1:
    elves = reduce(elves)

print(elves[0][0])