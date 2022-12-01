import file_loader

input_string = file_loader.get_input()

def get_abas(s):
    abas = []
    for a, b, c in zip(s, s[1:], s[2:]):
        if a == c and a != b:
            abas.append(a+b+c)
    return abas

def has_bab(s, aba):
    bab = aba[1] + aba[0] + aba[1]
    return bab in s


import re
def has_ssl(s):
    split = re.split("\\[|\\]", s)
    outers = []
    inners = []
    for i, s in enumerate(split):
        if i%2 == 1:
            inners.append(s)
        else:
            outers.append(s)
    abas = []
    for outer in outers:
        abas += get_abas(outer)
    
    for inner in inners:
        for aba in abas:
            if has_bab(inner, aba):
                return True
    return False
        

count = 0
for line in input_string.splitlines():
    if has_ssl(line):
        count += 1

print(count)