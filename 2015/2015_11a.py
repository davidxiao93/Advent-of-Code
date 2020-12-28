import string

input = """cqjxjnds"""

def has_increasing_digits(l):
    for a, b, c in zip(l, l[1:], l[2:]):
        if a+1 == b and b+1 == c:
            return True
    return False

def has_no_bad_chars(l):
    for c in ['i', 'o', 'l']:
        if string.ascii_lowercase.index(c) in l:
            return False
    return True

def has_distinct_pairs(l):
    should_skip = False
    count = 0
    for a, b in zip(l, l[1:]):
        if should_skip:
            should_skip = False
            continue
        if a == b:
            should_skip = True
            count += 1
        if count >= 2:
            return True

    return False

def is_valid(l):
    return has_no_bad_chars(l) and has_distinct_pairs(l) and has_increasing_digits(l)

def increment(l):
    index = -1
    l[index] += 1
    while l[index] == 26:
        l[index] = 0
        index -= 1
        if index * -1 > len(l):
            l = [0] + l
            return l
        l[index] += 1

    for i, j in enumerate(l):
        if j in [8, 11, 14]:
            l[i] +=1
            for k in range(i+1, len(l)):
                l[k] = 0
            break


    return l

def string_to_list(s):
    return [string.ascii_lowercase.index(c) for c in s]

def list_to_string(l):
    return "".join([string.ascii_lowercase[i] for i in l])




l = string_to_list(input)
while not is_valid(l):
    increment(l)

print(list_to_string(l))


