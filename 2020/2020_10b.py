input = """48
171
156
51
26
6
80
62
65
82
130
97
49
31
142
83
75
20
154
119
56
114
92
33
140
74
118
1
96
44
128
134
121
64
158
27
17
101
59
12
89
88
145
167
11
3
39
43
105
16
170
63
111
2
108
21
146
77
45
52
32
127
147
76
58
37
86
129
57
133
120
163
138
161
139
71
9
141
168
164
124
157
95
25
38
69
87
155
135
15
102
70
34
42
24
50
68
169
10
55
117
30
81
151
100
162
148"""


#
# input = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""
#
# input = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""

values = [-3, 0] + sorted([int(x) for x in input.splitlines()])
values = values + [max(values)+3]

"""

Insight: Where there is a difference of 3, that must be kept
-> break the sequence down where there is a difference of 3
"""

all_groups = []
while len(values) != 0:
    counter = 1
    while counter + 1 < len(values) and values[counter + 1] - values[counter] != 3:
        counter += 1
    all_groups.append(values[:counter + 2])
    values = values[counter:]

print(all_groups)

patterns = {}
for group in all_groups:
    # convert into diff pattern
    p = tuple()
    for a, b in zip(group, group[1:]):
        p += tuple([b - a])
    if len(p) != 0:
        if p not in patterns:
            patterns[p] = 0
        patterns[p] += 1

"""

patterns are like (3, 1, 1, 3)

"""
print(patterns)


# mapping from number of 1-diffs to possibilities
ones = {
    0: 1,
    1: 1,
    2: 2
}

max_ones = 0
for p in patterns:
    if p.count(1) > max_ones:
        max_ones = p.count(1)

for i in range(max_ones + 1):
    if i not in ones:
        ones[i] = 2*ones[i - 1]
        if i - 4 in ones:
            ones[i] -= ones[i-4]

combo = 1
for p, quantity in patterns.items():
    combo *= ones[p.count(1)] ** quantity

print(combo)






