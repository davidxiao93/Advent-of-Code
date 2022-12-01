import file_loader

input_string = file_loader.get_input()

def has_repeated_pair(s):
    for i in range(0, len(s) - 1):
        sub = s[i:i+2]
        check = s[i+2:]
        if sub in check:
            return True

    return False


def has_aba_pattern(s):
    for i in range(0, len(s) - 2):
        a1 = s[i]
        a2 = s[i+2]
        if a1 == a2:
            return True
    return False


print(len([s for s in input_string.split()
           if has_repeated_pair(s)
           and has_aba_pattern(s)
           ]))