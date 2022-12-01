import file_loader

input_string = file_loader.get_input()



class Ingredient:
    def __init__(self, name, capacity, durability, flavour, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavour = flavour
        self.texture = texture
        self.calories = calories

    def score(self):
        return \
        (self.capacity if self.capacity > 0 else 0) \
        * (self.durability if self.durability > 0 else 0) \
        * (self.flavour if self.flavour > 0 else 0) \
        * (self.texture if self.texture > 0 else 0)

ingredients = []

def multiply_ingredient(quantity, ingredient):
    return Ingredient(
        str(quantity) + " * " + ingredient.name,
        quantity * ingredient.capacity,
        quantity * ingredient.durability,
        quantity * ingredient.flavour,
        quantity * ingredient.texture,
        quantity * ingredient.calories
    )

def mix_ingredient(i1, i2):
    return Ingredient(
        "(" + i1.name + " and " + i2.name + ")",
        i1.capacity + i2.capacity,
        i1.durability + i2.durability,
        i1.flavour + i2.flavour,
        i1.texture + i2.texture,
        i1.calories + i2.calories,
    )


for line in input_string.split("\n"):
    words = line.split()
    ingredients.append(
        Ingredient(
            words[0][:-1],
            int(words[2][:-1]),
            int(words[4][:-1]),
            int(words[6][:-1]),
            int(words[8][:-1]),
            int(words[10])
        )
    )


mapping = {}
best_score = 0
for a in range(100):
    for b in range(0, 100 - a):
        for c in range(0, 100 - a - b):
            d = 100 - a - b - c
            mixed = mix_ingredient(
                mix_ingredient(
                    multiply_ingredient(a, ingredients[0]),
                    multiply_ingredient(b, ingredients[1])
                ),
                mix_ingredient(
                    multiply_ingredient(c, ingredients[2]),
                    multiply_ingredient(d, ingredients[3])
                )
            )
            if mixed.calories != 500:
                continue
            score = mixed.score()
            if score > best_score:
                best_score = score

print(best_score)
















