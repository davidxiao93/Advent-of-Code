import file_loader

input_string = file_loader.get_input()

elves_inventory = {i: sum([int(x) for x in inventory.split("\n")]) for i, inventory in enumerate(input_string.split("\n\n"))}

max_inventory = max(elves_inventory.values())

print(max_inventory)
