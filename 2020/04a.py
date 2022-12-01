import file_loader

input_string = file_loader.get_input()

count = 0
for passport in input_string.split("\n\n"):
    key_values = passport.split()
    is_valid = True
    keys = [kv.split(":")[0] for kv in key_values]
    for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if key not in keys:
            is_valid = False

    if is_valid:
        count += 1

print(count)