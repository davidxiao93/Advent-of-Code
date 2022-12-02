import file_loader

input_string = file_loader.get_input()

# input_string = """0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb"""

from itertools import product


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

while len(unexpanded_rules) > 0:
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


valid_for_rule_zero = expanded_rules[0]

print(sum([
    1
    for message in messages.splitlines()
    if message in valid_for_rule_zero
]))







