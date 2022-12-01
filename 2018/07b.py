import file_loader

input_string = file_loader.get_input()
max_workers = 5
task_penalty = 60


# input_string = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin."""
# max_workers = 2
# task_penalty = 0


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



workers = {}
time_taken = 0
while len(steps_to_take) != 0:

    next_steps = sorted([
        s
        for s in steps_to_take
        if s not in dependencies
           or 0 == len(dependencies[s])
    ])

    for c in next_steps:
        if c not in workers and len(workers) != max_workers:
            workers[c] = ord(c) - 64 + task_penalty

    # print(workers)

    completed_tasks = set()
    for task in workers:
        workers[task] = workers[task] - 1
        if workers[task] == 0:
            completed_tasks.add(task)
    time_taken += 1
    for c in completed_tasks:
        workers.pop(c, None)
        # remove dependency on c as it is now taken
        steps_taken.append(c)
        steps_to_take.remove(c)
        if c in depends_on:
            for d in depends_on[c]:
                dependencies[d].remove(c)


print(time_taken)