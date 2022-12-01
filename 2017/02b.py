import file_loader

input_string = file_loader.get_input()



def find_evenly_divisible(xs):
    x_set = set(xs)
    for x in sorted(xs):
        x_set.remove(x)
        for y in x_set:
            if y % x == 0:
                return int(y / x)
    print("not found")
    exit(0)

checksum = 0
for line in input_string.splitlines():
    values = { int(x) for x in line.split() }
    checksum += find_evenly_divisible(values)

print(checksum)