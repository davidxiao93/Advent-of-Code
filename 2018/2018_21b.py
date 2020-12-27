input = """#ip 4
seti 123 0 3
bani 3 456 3
eqri 3 72 3
addr 3 4 4
seti 0 0 4
seti 0 5 3
bori 3 65536 5
seti 5557974 2 3
bani 5 255 2
addr 3 2 3
bani 3 16777215 3
muli 3 65899 3
bani 3 16777215 3
gtir 256 5 2
addr 2 4 4
addi 4 1 4
seti 27 9 4
seti 0 0 2
addi 2 1 1
muli 1 256 1
gtrr 1 5 1
addr 1 4 4
addi 4 1 4
seti 25 4 4
addi 2 1 2
seti 17 6 4
setr 2 2 5
seti 7 1 4
eqrr 3 0 2
addr 2 4 4
seti 5 7 4"""


"""
    00 seti 123 0 3         --- r[3] = 123
    01 bani 3 456 3         --- r[3] = r[3] & 456
    02 eqri 3 72 3          --- r[3] = 1 if r[3] == 72 else 0
    03 addr 3 4 4           === r[4] += r[3]
    04 seti 0 0 4           === r[4] = 0, next is 1
    Above is executed once
    05 seti 0 5 3           --- r[3] = 0
30
    06 bori 3 65536 5       --- r[5] = r[3] | 65536
    07 seti 5557974 2 3     --- r[3] = 5557974
27
    08 bani 5 255 2         --- r[2] = r[5] & 255 
    09 addr 3 2 3           --- r[3] += r[2]
    10 bani 3 16777215 3    --- r[3] = r[3] & 16777215
    11 muli 3 65899 3       --- r[3] *= 65899
    12 bani 3 16777215 3    --- r[3] = r[3] & 16777215
    13 gtir 256 5 2         --- r[2] = 1 if 256 > r[5] else 0
    14 addr 2 4 4           === r[4] += r[2]
    15 addi 4 1 4           === r[4] += 1, next is 17
    16 seti 27 9 4          === r[4] = 27, next is 28 
    
    17 seti 0 0 2           --- r[2] = 0
25
    18 addi 2 1 1           --- r[1] = r[2] + 1
    19 muli 1 256 1         --- r[1] *= 256
    20 gtrr 1 5 1           --- r[1] = 1 if r[1] > r[5] else 0
    21 addr 1 4 4           === r[4] += r[1]
    22 addi 4 1 4           === r[4] += 1, next is 24
    23 seti 25 4 4          === r[4] = 25, next is 26
    24 addi 2 1 2           --- r[2] += 1
    25 seti 17 6 4          === r[4] = 17, next is 18
                            at this point, r[2] = r[5] // 256
    26 setr 2 2 5           --- r[5] = r[2]
    27 seti 7 1 4           === r[4] = 7, next is 8
    28 eqrr 3 0 2           --- r[2] = 1 if r[3] == r[0] else 0
    29 addr 2 4 4           === r[4] += r[2]
    30 seti 5 7 4           === r[4] = 5, next is 6

"""


"""
translating the program into something closer to python

r[5] = 65536
r[3] = 5557974
while True:
    r[3] = (r[3] + (r[5] % 256)) * 65899 % 16777216
    if r[5] < 256:
        if r[3] == r[0]:
            break
        r[5] = r[3] | 65536
        r[3] = 5557974
    else:
        r[5] = r[5] // 256


We want the maximal number of instructions to be called
Thus, we want to go through the r[3] == r[0] check as many times as possible, 
but one of the r[3] values must be r[0] eventually to make sure it halts
Therefore, we want to find the value before the first duplicate in the sequence of r[3]
"""

r_5 = 65536
r_3 = 5557974
seen_outputs = []
while True:
    r_3 = (r_3 + (r_5 % 256)) * 65899 % 16777216
    if r_5 < 256:
        if r_3 in seen_outputs:
            print(seen_outputs[-1])
            break
        seen_outputs.append(r_3)
        r_5 = r_3 | 65536
        r_3 = 5557974
    else:
        r_5 = r_5 // 256