import file_loader

input_string = file_loader.get_input()

# input_string = """0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5"""

directly_connected_to = {}

for line in input_string.splitlines():
    left, right = line.split(" <-> ")
    directly_connected_to[int(left)] = {int(x) for x in right.split(",")}


def get_connected_to(s, acc):
    for a in directly_connected_to[s]:
        if a not in acc:
            acc |= get_connected_to(a, acc | {a})
    acc |= directly_connected_to[s]
    return acc

print(len(get_connected_to(0, set())))
