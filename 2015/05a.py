import file_loader

input_string = file_loader.get_input()

def has_three_vowels(s):
    return len([c for c in s
                if c in ['a', 'e', 'i', 'o', 'u']]
               ) >= 3

def has_double_char(s):
    for i, c in enumerate(s):
        if i + 1 == len(s):
            return False
        if c == s[i+1]:
            return True
    return False

def has_allowed_substrings(s):
    return len([x for x in ["ab", "cd", "pq", "xy"]
                if x in s
                ]) == 0


print(len([s for s in input_string.split()
           if has_three_vowels(s)
           and has_double_char(s)
           and has_allowed_substrings(s)
           ]))