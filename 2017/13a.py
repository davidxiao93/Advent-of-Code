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

time = -1
severity = 0
while time <= max(depth_to_range):
    time += 1
    if time in depth_to_range:
        if scanner_pos(time, depth_to_range[time]) == 0:
            # print("caught at", time)
            severity += time * depth_to_range[time]

print(severity)



