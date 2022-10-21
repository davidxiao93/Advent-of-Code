from typing import Dict

input = """1 JNDQ, 11 PHNC => 7 LBJSB
1 BFKR => 9 VGJG
11 VLXQL => 5 KSLFD
117 ORE => 6 DMSLX
2 VGJG, 23 MHQGW => 6 HLVR
2 QBJLJ => 6 DBJZ
1 CZDM, 21 ZVPJT, 1 HLVR => 5 VHGQP
1 RVKX => 1 FKMQD
38 PHNC, 10 MHQGW => 5 GMVJX
4 CZDM, 26 ZVHX => 7 QBGQB
5 LBJSB, 2 DFZRS => 4 QBJLJ
4 TJXZM, 11 DWXW, 14 VHGQP => 9 ZBHXN
20 VHGQP => 8 SLXQ
1 VQKM => 9 BDZBN
115 ORE => 4 BFKR
1 VGJG, 1 SCSXF => 5 PHNC
10 NXZXH, 7 ZFXP, 7 ZCBM, 7 MHNLM, 1 BDKZM, 3 VQKM => 5 RMZS
147 ORE => 2 WHRD
16 CQMKW, 8 BNJK => 5 MHNLM
1 HLVR => 5 TJQDC
9 GSLTP, 15 PHNC => 5 SFZTF
2 MJCD, 2 RVKX, 4 TJXZM => 1 MTJSD
1 DBJZ, 3 SLXQ, 1 GMSB => 9 MGXS
1 WZFK => 8 XCMX
1 DFZRS => 9 GSLTP
17 PWGXR => 2 DFZRS
4 BFKR => 7 JNDQ
2 VKHN, 1 SFZTF, 2 PWGXR => 4 JDBS
2 ZVPJT, 1 PHNC => 6 VQKM
18 GMSB, 2 MGXS, 5 CQMKW => 3 XGPXN
4 JWCH => 3 BNJK
1 BFKR => 2 PWGXR
12 PHNC => 2 GMSB
5 XGPXN, 3 VQKM, 4 QBJLJ => 9 GXJBW
4 MHQGW => 9 DWXW
1 GMSB, 1 BFKR => 5 DBKC
1 VLXQL, 10 KSLFD, 3 JWCH, 7 DBKC, 1 MTJSD, 2 WZFK => 9 GMZB
4 JDBS => 8 BRNWZ
2 ZBHXN => 7 HMNRT
4 LBJSB => 7 BCXGX
4 MTJSD, 1 SFZTF => 8 ZCBM
12 BRNWZ, 4 TJXZM, 1 ZBHXN => 7 WZFK
10 HLVR, 5 LBJSB, 1 VKHN => 9 TJXZM
10 BRNWZ, 1 MTJSD => 6 CMKW
7 ZWHT => 7 VKHN
5 CQMKW, 2 DBKC => 6 ZFXP
1 CMKW, 5 JNDQ, 12 FKMQD, 72 BXZP, 28 GMVJX, 15 BDZBN, 8 GMZB, 8 RMZS, 9 QRPQB, 7 ZVHX => 1 FUEL
10 MGXS => 9 JWCH
1 BFKR => 8 SCSXF
4 SFZTF, 13 CZDM => 3 RVKX
1 JDBS, 1 SFZTF => 9 TSWV
2 GMVJX, 1 PHNC => 1 CZDM
6 JDBS => 1 BXZP
9 TSWV, 5 TJXZM => 8 NXZXH
1 HMNRT, 5 TSWV => 4 VLXQL
16 WZFK, 11 XCMX, 1 GXJBW, 16 NXZXH, 1 QBGQB, 1 ZCBM, 10 JWCH => 3 QRPQB
12 SCSXF, 6 VGJG => 4 ZVPJT
10 JNDQ => 3 ZWHT
1 DBJZ, 9 BCXGX => 2 CQMKW
1 WHRD, 14 DMSLX => 8 MHQGW
3 VKHN, 8 TJQDC => 4 MJCD
1 QBJLJ => 4 ZVHX
1 MHQGW, 4 ZVHX => 3 BDKZM"""

class Ingredient:
    def __init__(self, name):
        self.name = name
        self.recipe_ingredients = {}
        self.recipe_quantity_produced = 1


ingredients = {}

for line in input.splitlines():
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
ore_required = 0
while len(to_break_down) != 0:
    next_ingredient, required_quantity = pop_next(to_break_down)
    if required_quantity % next_ingredient.recipe_quantity_produced == 0:
        multiplier = required_quantity // next_ingredient.recipe_quantity_produced
    else:
        multiplier = 1 + (required_quantity // next_ingredient.recipe_quantity_produced)
    for ingredient, recipe_quanity in next_ingredient.recipe_ingredients.items():
        if ingredient.name == "ORE":
            ore_required += multiplier * recipe_quanity
        else:
            if ingredient not in to_break_down:
                to_break_down[ingredient] = 0
            to_break_down[ingredient] += multiplier * recipe_quanity

print(ore_required)


