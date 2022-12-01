from typing import Dict

import file_loader

input_string = file_loader.get_input()


class Ingredient:
    def __init__(self, name):
        self.name = name
        self.recipe_ingredients = {}
        self.recipe_quantity_produced = 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


ingredients = {}

for line in input_string.splitlines():
    left, right = line.split("=>")
    name = right.split()[1].strip()
    recipe_quantity_produced = int(right.split()[0])
    recipe_ingredients = {
            s.split()[1].strip(): int(s.split()[0])
            for s in left.split(",")
        }
    if name not in ingredients:
        ingredients[name] = Ingredient(name)
    i = ingredients[name]
    i.recipe_quantity_produced = recipe_quantity_produced
    for i_name, i_quantity in recipe_ingredients.items():
        if i_name not in ingredients:
            ingredients[i_name] = Ingredient(i_name)
        i.recipe_ingredients[ingredients[i_name]] = i_quantity

fuel = ingredients["FUEL"]

"""
need to define an ordering for how to reduce this into ore
current idea: ordering is based upon the maximum distance in tree to the FUEL root
"""

depths = {}
values_to_check = { ("FUEL", 0) }
while len(values_to_check) != 0:
    name, depth = values_to_check.pop()
    if name not in depths:
        depths[name] = depth
    else:
        depths[name] = max(depths[name], depth)

    for ingredient in ingredients[name].recipe_ingredients:
        values_to_check.add((ingredient.name, depth + 1))

ingredient_order = sorted(ingredients.keys(), key=lambda k: depths[k])

"""
ingredients with lower depths should be expanded first
order does not matter when depths are equal
can build a sort order
"""

def pop_next(dict: Dict[Ingredient, int]):
    min_ingredient = min(dict, key=lambda i: depths[i.name])
    quantity = dict[min_ingredient]
    dict.pop(min_ingredient, None)
    return min_ingredient, quantity


to_break_down = {
    ingredients["FUEL"]: 1
}
one_cycle_surplus = {}
ore_required = 0
while len(to_break_down) != 0:
    next_ingredient, required_quantity = pop_next(to_break_down)
    if required_quantity % next_ingredient.recipe_quantity_produced == 0:
        multiplier = required_quantity // next_ingredient.recipe_quantity_produced
    else:
        multiplier = 1 + (required_quantity // next_ingredient.recipe_quantity_produced)
    if next_ingredient not in one_cycle_surplus:
        one_cycle_surplus[next_ingredient] = 0
    one_cycle_surplus[next_ingredient] += (multiplier * next_ingredient.recipe_quantity_produced) - required_quantity
    for ingredient, recipe_quanity in next_ingredient.recipe_ingredients.items():
        if ingredient.name == "ORE":
            ore_required += multiplier * recipe_quanity
        else:
            if ingredient not in to_break_down:
                to_break_down[ingredient] = 0
            to_break_down[ingredient] += multiplier * recipe_quanity


"""
requires ore_required pieces of ore to produce 1 fuel
but this also produces everything in surplusses
idea:
- calculate how much surplusses we would have if we converted as much ore as possible without using any surplusses
- then "break down" the surplusses back into ore
- start again with the remaining ore
- repeat until no more fuel can be created
"""

fuel_created = 0
remaining_ore = 1_000_000_000_000
surplus = {}
last_fuel_created = -1

while last_fuel_created != fuel_created:
    last_fuel_created = fuel_created
    new_fuel = remaining_ore // ore_required
    fuel_created += new_fuel
    remaining_ore -= new_fuel * ore_required
    for i, v in one_cycle_surplus.items():
        if i.name not in surplus:
            surplus[i.name] = 0
        surplus[i.name] += new_fuel * v
    for i_name in ingredient_order:
        if i_name not in surplus:
            continue
        if i_name == "ORE":
            continue
        ingredient = ingredients[i_name]
        extra_quantity = surplus[i_name]
        multiplier = extra_quantity // ingredient.recipe_quantity_produced
        surplus[i_name] -= multiplier * ingredient.recipe_quantity_produced
        for ii, ii_quanitity in ingredient.recipe_ingredients.items():
            if ii.name == "ORE":
                remaining_ore += multiplier * ii_quanitity
            else:
                if ii.name not in surplus:
                    surplus[ii.name] = 0
                surplus[ii.name] += multiplier * ii_quanitity


print(fuel_created)
