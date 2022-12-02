import file_loader

input_string = file_loader.get_input()

from itertools import product

input_string = input_string.replace("8: 42", "8: 42 | 42 8").replace("11: 42 31", "11: 42 31 | 42 11 31")
rules, messages = input_string.split("\n\n")

unexpanded_rules = {}
expanded_rules = {}




for rule in rules.splitlines():
    key, expression = rule.split(": ")
    if "\"" in expression:
        expanded_rules[int(key)] = { expression[1] }
    else:
        expressions = expression.split("|")
        unexpanded_rules[int(key)] = [
            [
                int(x)
                for x in e.split()
            ]
            for e in expressions
        ]

# expand all the ones that can be expanded without loops
last_len = 0
while len(unexpanded_rules) != last_len:
    last_len = len(unexpanded_rules)
    expandable_keys = set()
    for key, expressions in unexpanded_rules.items():
        can_be_expanded = True
        for expression in expressions:
            for e in expression:
                if e not in expanded_rules:
                    can_be_expanded = False
        if can_be_expanded:
            expandable_keys.add(key)
    for key in expandable_keys:
        expanded_rules[key] = set()
        for expression in unexpanded_rules[key]:
            parts = [expanded_rules[e] for e in expression]
            for p in product(*parts):
                expanded_rules[key].add("".join(p))
        unexpanded_rules.pop(key, None)

# luckily for us, the only rules unexpanded are 0 and the ones with loops (8 and 11)
# rule  0 => 8 11
# rule  8 => 42 | 42 8
# rule 11 => 42 31 | 42 11 31
# In summary, 0 must be formed of some number of 42s, and then X amount of 42s followed by X amount of 31s
# Put another way, 0 must be formed of Y 42s and then X 31s and Y > X, Y >= 2 and X >= 1
# Moreover, there is no overlap between the valid values of rule 42 and rule 31!
# Additionally, all valid values of either rule 42 or 31 are 8 chars long

def is_valid(s: str):
    blocks = len(next(iter(expanded_rules[42])))
    if len(s) % blocks != 0:
        # a valid string must be formed of some number of blocks of 8 chars
        return False

    rule_42 = expanded_rules[42]
    rule_31 = expanded_rules[31]

    # count how many times a block of 8 chars at the start of s fits into rule 42
    count_42 = 0
    while s[:blocks] in rule_42:
        count_42 += 1
        s = s[blocks:]

    # after the blocks of rule 42, now comes rule 31
    # count how many times a block of 8 chars now at the start of s fits into rule 31
    count_31 = 0
    while s[:blocks] in rule_31:
        count_31 += 1
        s = s[blocks:]

    if len(s) != 0:
        # If there are any left over characters, then s did not match the pattern
        return False

    if count_42 <= 1:
        # Not enough rule 42 matches
        return False

    if count_31 == 0:
        # Not enough rule 31 matches
        return False

    if count_42 <= count_31:
        # Not enough rule 42 matches as there needs to be strictly more rule 42 matches
        return False

    return True


print(sum([
    1
    for m in messages.splitlines()
    if is_valid(m)
]))



