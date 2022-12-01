import file_loader

input_string = file_loader.get_input()

known_details = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


class Sue:
    def __init__(self, id, details):
        self.id = id
        self.details = details

    def matches(self):
        for key, value in known_details.items():
            if key in self.details:
                if key == "trees" or key == "cats":
                    if self.details[key] <= known_details[key]:
                        return False
                elif key == "pomeranians" or key == "goldfish":
                    if self.details[key] >= known_details[key]:
                        return False
                elif self.details[key] != known_details[key]:
                    return False
        return True

sues = []
for line in input_string.splitlines():
    sue_id, all_values = line.split(":", 1)
    id = sue_id.split()[-1]
    values = all_values.split(",")
    d = {}
    for value in values:
        k = value.split(":")[0].strip()
        v = int(value.split(":")[-1].strip())
        d[k] = v
    sues.append(Sue(id, d))

potential_sues = [sue for sue in sues if sue.matches()]

print([sue.id for sue in potential_sues][0])