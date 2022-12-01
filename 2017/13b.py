import file_loader

input_string = file_loader.get_input()

# input_string = """0: 3
# 1: 2
# 4: 4
# 6: 4"""

depth_to_range = {}

for line in input_string.splitlines():
    depth, range = (int(x) for x in line.split(":", 1))
    depth_to_range[depth] = range


def scanner_pos(t, r):
    p = t % (2 * r - 2)
    if p >= (r - 1):
        p = (2 * r - 2) - p
    return p


def is_caught(delay):

    for depth, range in depth_to_range.items():
        if scanner_pos(depth + delay, range) == 0:
            # print("caught at", time)
            return True
    return False


caught = True
d = -1
while caught:
    d += 1
    # print("testing", d)
    caught = is_caught(d)
print(d)



