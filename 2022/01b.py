import file_loader

input_string = file_loader.get_input()

elves_inventory = {i: sum([int(x) for x in inventory.split("\n")]) for i, inventory in enumerate(input_string.split("\n\n"))}
print(sum(sorted(elves_inventory.values(), reverse=True)[:3]))
