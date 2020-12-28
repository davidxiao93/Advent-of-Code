input = """0: 3
1: 2
2: 4
4: 4
6: 5
8: 6
10: 8
12: 8
14: 6
16: 6
18: 8
20: 8
22: 6
24: 12
26: 9
28: 12
30: 8
32: 14
34: 12
36: 8
38: 14
40: 12
42: 12
44: 12
46: 14
48: 12
50: 14
52: 12
54: 10
56: 14
58: 12
60: 14
62: 14
66: 10
68: 14
74: 14
76: 12
78: 14
80: 20
86: 18
92: 14
94: 20
96: 18
98: 17"""

# input = """0: 3
# 1: 2
# 4: 4
# 6: 4"""

depth_to_range = {}

for line in input.splitlines():
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



