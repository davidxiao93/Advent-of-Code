import file_loader

input_string = file_loader.get_input()


allergen_mapping = {}

for line in input_string.splitlines():
    ingredients = line.split("(")[0].split()
    allergens = [a.strip() for a in line.split("(")[1][9:-1].split(",")]
    for a in allergens:
        if a not in allergen_mapping:
            allergen_mapping[a] = set(ingredients)
        else:
            allergen_mapping[a] &= set(ingredients)


seen_ingredients = set()
final_allergen_mapping = {}
while len(allergen_mapping) != 0:
    allergens_to_remove = []
    for allergen in allergen_mapping:
        allergen_mapping[allergen] -= seen_ingredients
        if len(allergen_mapping[allergen]) == 0:
            allergens_to_remove.append(allergen)
        elif len(allergen_mapping[allergen]) == 1:
            final_allergen_mapping[allergen] = allergen_mapping[allergen].pop()
            seen_ingredients.add(final_allergen_mapping[allergen])
    for allergen in allergens_to_remove:
        allergen_mapping.pop(allergen, None)


canonical_dangerous_ingredient_list = []
for allergen in sorted(final_allergen_mapping.keys()):
    canonical_dangerous_ingredient_list.append(final_allergen_mapping[allergen])


print(",".join(canonical_dangerous_ingredient_list))


