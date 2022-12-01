import file_loader

input_string = file_loader.get_input()


orbits = {}

for line in input_string.splitlines():
    l, r = line.split(")")
    orbits[r] = l


def get_orbital_path(target):
    path = []
    current = target
    while current != "COM":
        path.append(current)
        current = orbits[current]
    path.append(current)
    return path

my_path = get_orbital_path("YOU")
santa_path = get_orbital_path("SAN")

# remove common ancestors in path
while my_path[-2] == santa_path[-2]:
    my_path = my_path[:-1]
    santa_path = santa_path[:-1]

assert(my_path[-1] == santa_path[-1])

print(
    len(my_path) + len(santa_path)
    - 1 # remove YOU from path
    - 1 # remove SAN from path
    - 1 # remove the duplicate shared parent
    - 1 # want number of transfers, not number of places
)



