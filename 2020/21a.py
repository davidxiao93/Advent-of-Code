import file_loader

input_string = file_loader.get_input()


ingredient_count = {}
allergen_mapping = {}

for line in input_string.splitlines():
    ingredients = line.split("(")[0].split()
    allergens = [a.strip() for a in line.split("(")[1][9:-1].split(",")]
    for i in ingredients:
        if i not in ingredient_count:
            ingredient_count[i] = 0
        ingredient_count[i] += 1
    for a in allergens:
        if a not in allergen_mapping:
            allergen_mapping[a] = set(ingredients)
        else:
            allergen_mapping[a] &= set(ingredients)

print(sum([
    count
    for ingredient, count in ingredient_count.items()
    if ingredient not in set.union(*allergen_mapping.values())
]))

