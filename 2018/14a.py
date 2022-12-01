import file_loader

input_string = file_loader.get_input()
input_string = int(input_string)


recipes = [3,7]
elfA = 0
elfB = 1

def get_new_recipes(a, b):
    return [int(x) for x in str(a + b)]

def pretty_print(recipes, elfA, elfB):
    row = []
    for i, r in enumerate(recipes):
        if i == elfA:
            row.append("a")
        else:
            row.append(" ")
        row.append(str(r))
        if i == elfB:
            row.append("b")
        else:
            row.append(" ")
    print(" ".join(row))


# pretty_print(recipes, elfA, elfB)
while len(recipes) < input_string + 10:
    recipes += get_new_recipes(recipes[elfA], recipes[elfB])
    elfA = (elfA + 1 + recipes[elfA]) % len(recipes)
    elfB = (elfB + 1 + recipes[elfB]) % len(recipes)
    # pretty_print(recipes, elfA, elfB)

print("".join(str(i) for i in recipes[input_string:input_string + 10]))