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
programs = set()

for line in input_string.splitlines():
    left, right = line.split(" <-> ")
    r_programs = {int(x) for x in right.split(",")}
    directly_connected_to[int(left)] = r_programs
    programs |= r_programs
    programs |= {int(left)}


def get_connected_to(s, acc):
    for a in directly_connected_to[s]:
        if a not in acc:
            acc |= get_connected_to(a, acc | {a})
    acc |= directly_connected_to[s]
    return acc


count = 0
while len(programs) > 0:
    p = programs.pop()
    connected = get_connected_to(p, set())
    programs -= connected
    count += 1

print(count)