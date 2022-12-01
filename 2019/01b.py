import file_loader

input_string = file_loader.get_input()


def fuel_for_module(mass):
    fuel_for_mass = (mass // 3) - 2
    fuel_to_fuel = fuel_for_mass
    while True:
        additional_fuel = (fuel_to_fuel // 3) - 2
        if additional_fuel <= 0:
            break
        else:
            fuel_for_mass += additional_fuel
            fuel_to_fuel = additional_fuel
    return fuel_for_mass

total_fuel = 0
for line in input_string.splitlines():
    mass = int(line)
    total_fuel += fuel_for_module(mass)



print(total_fuel)