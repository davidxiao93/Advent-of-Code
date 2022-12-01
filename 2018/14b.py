import file_loader

input_string = file_loader.get_input()


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

def found(recipes, target_str):
    recipes_str = "".join(str(d) for d in recipes)
    if target_str in recipes_str:
        return recipes_str.index(target_str)
    return None


# pretty_print(recipes, elfA, elfB)
counter = 0
last_size = 0
while True:
    recipes += get_new_recipes(recipes[elfA], recipes[elfB])
    elfA = (elfA + 1 + recipes[elfA]) % len(recipes)
    elfB = (elfB + 1 + recipes[elfB]) % len(recipes)
    if counter % 1000 == 0:
        # No need to check on every iteration because the list of recipes is only being added to
        new_size = len(recipes)
        f = found(recipes[max(0, last_size - len(input_string)):], input_string)
        if f is not None:
            print(f + max(0, last_size - len(input_string)))
            break
        last_size = new_size
    counter += 1
    # pretty_print(recipes, elfA, elfB)
