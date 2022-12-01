import file_loader

input_string = file_loader.get_input()

def twos_threes(s):
    char_dict = {}
    for c in s:
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return 2 in char_dict.values(), 3 in char_dict.values()

twos = 0
threes = 0
for line in input_string.splitlines():
    two, three = twos_threes(line)
    twos += two
    threes += three

print(twos * threes)