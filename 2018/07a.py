import file_loader

input_string = file_loader.get_input()

steps_to_take = set()
steps_taken = []
depends_on = {}
dependencies = {}

for line in input_string.splitlines():
    words = line.split()
    steps_to_take.add(words[1])
    steps_to_take.add(words[7])
    if words[1] not in depends_on:
        depends_on[words[1]] = set()
    depends_on[words[1]].add(words[7])
    if words[7] not in dependencies:
        dependencies[words[7]] = set()
    dependencies[words[7]].add(words[1])

while len(steps_to_take) != 0:
    next_step = sorted([
        s
        for s in steps_to_take
        if s not in dependencies
           or 0 == len(dependencies[s])
    ])[0]
    # remove dependency on next_step as it is now taken
    steps_taken.append(next_step)
    steps_to_take.remove(next_step)
    if next_step in depends_on:
        for d in depends_on[next_step]:
            dependencies[d].remove(next_step)

print("".join(steps_taken))