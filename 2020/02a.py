import file_loader

input_string = file_loader.get_input()

def is_valid(s, c, minimum, maxinum):
    count = s.count(c)
    return minimum <= count and count <= maxinum


count = 0
for line in input_string.split("\n"):
    rule, password = line.split(":")

    quantity, char = rule.split()
    values = quantity.split("-")

    if is_valid(password.strip(), char, int(values[0]), int(values[1])):
        count += 1


print(count)