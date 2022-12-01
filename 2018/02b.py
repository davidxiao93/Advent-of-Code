import file_loader

input_string = file_loader.get_input()

from itertools import combinations

def is_similar(a, b):
    if len(a) != len(b):
        return False
    count = 0
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y:
            count += 1
    if count != len(a) - 1:
        return False
    return True

def get_similarities(a, b):
    c = ""
    for x, y in zip(a, b):
        if x == y:
            c += x
    return c


for a, b in combinations(input_string.splitlines(), 2):
    if is_similar(a, b):
        print(get_similarities(a, b))
        break

