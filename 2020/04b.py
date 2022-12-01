import file_loader

input_string = file_loader.get_input()




rules = {
    "byr": lambda v: len(v) == 4
                     and v.isnumeric()
                     and 1920 <= int(v) <= 2002,
    "iyr": lambda v: len(v) == 4
                     and v.isnumeric()
                     and 2010 <= int(v) <= 2020,
    "eyr": lambda v: len(v) == 4
                     and v.isnumeric()
                     and 2020 <= int(v) <= 2030,
    "hgt": lambda v: v[:-2].isnumeric()
                     and (v[-2:] == "cm" or v[-2:] == "in")
                     and ((150 <= int(v[:-2]) <= 193)
                        if v[-2:] == "cm" else
                            (59 <= int(v[:-2]) <= 76)),
    "hcl": lambda v: len(v) == 7
                     and v.startswith("#")
                     and 6 == sum([1 if c in [
                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"
                        ] else 0 for c in v[1:]]),
    "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda v: len(v) == 9
                     and v.isnumeric()
}


count = 0
for passport in input_string.split("\n\n"):
    key_values = passport.split()
    is_valid = True
    d = {kv.split(":")[0]: kv.split(":", 1)[-1] for kv in key_values}

    for key, rule in rules.items():
        if key not in d or not rule(d[key]):
            is_valid = False

    if is_valid:
        count += 1

print(count)