input = """Step B must be finished before step G can begin.
Step G must be finished before step J can begin.
Step J must be finished before step F can begin.
Step U must be finished before step Z can begin.
Step C must be finished before step M can begin.
Step Y must be finished before step I can begin.
Step Q must be finished before step A can begin.
Step N must be finished before step L can begin.
Step O must be finished before step A can begin.
Step Z must be finished before step T can begin.
Step I must be finished before step H can begin.
Step L must be finished before step W can begin.
Step F must be finished before step W can begin.
Step T must be finished before step X can begin.
Step A must be finished before step X can begin.
Step K must be finished before step X can begin.
Step S must be finished before step P can begin.
Step M must be finished before step E can begin.
Step E must be finished before step W can begin.
Step D must be finished before step P can begin.
Step P must be finished before step W can begin.
Step X must be finished before step H can begin.
Step V must be finished before step W can begin.
Step R must be finished before step H can begin.
Step H must be finished before step W can begin.
Step N must be finished before step I can begin.
Step X must be finished before step R can begin.
Step D must be finished before step V can begin.
Step V must be finished before step R can begin.
Step F must be finished before step K can begin.
Step P must be finished before step R can begin.
Step P must be finished before step V can begin.
Step S must be finished before step X can begin.
Step I must be finished before step S can begin.
Step J must be finished before step N can begin.
Step T must be finished before step S can begin.
Step T must be finished before step R can begin.
Step K must be finished before step P can begin.
Step N must be finished before step R can begin.
Step G must be finished before step T can begin.
Step I must be finished before step V can begin.
Step G must be finished before step Q can begin.
Step D must be finished before step H can begin.
Step V must be finished before step H can begin.
Step T must be finished before step K can begin.
Step T must be finished before step W can begin.
Step E must be finished before step H can begin.
Step C must be finished before step R can begin.
Step L must be finished before step K can begin.
Step G must be finished before step Y can begin.
Step Y must be finished before step O can begin.
Step O must be finished before step E can begin.
Step U must be finished before step S can begin.
Step X must be finished before step W can begin.
Step C must be finished before step D can begin.
Step E must be finished before step P can begin.
Step B must be finished before step R can begin.
Step F must be finished before step R can begin.
Step A must be finished before step D can begin.
Step G must be finished before step M can begin.
Step B must be finished before step Q can begin.
Step Q must be finished before step V can begin.
Step B must be finished before step W can begin.
Step S must be finished before step H can begin.
Step P must be finished before step X can begin.
Step I must be finished before step M can begin.
Step A must be finished before step S can begin.
Step M must be finished before step X can begin.
Step L must be finished before step S can begin.
Step S must be finished before step W can begin.
Step L must be finished before step V can begin.
Step Z must be finished before step X can begin.
Step M must be finished before step R can begin.
Step T must be finished before step A can begin.
Step N must be finished before step V can begin.
Step M must be finished before step H can begin.
Step E must be finished before step D can begin.
Step F must be finished before step V can begin.
Step B must be finished before step O can begin.
Step G must be finished before step U can begin.
Step J must be finished before step C can begin.
Step G must be finished before step F can begin.
Step Y must be finished before step M can begin.
Step F must be finished before step D can begin.
Step M must be finished before step P can begin.
Step F must be finished before step T can begin.
Step G must be finished before step A can begin.
Step G must be finished before step Z can begin.
Step K must be finished before step V can begin.
Step J must be finished before step Z can begin.
Step O must be finished before step Z can begin.
Step B must be finished before step E can begin.
Step Z must be finished before step V can begin.
Step Q must be finished before step O can begin.
Step J must be finished before step D can begin.
Step Y must be finished before step E can begin.
Step D must be finished before step R can begin.
Step I must be finished before step F can begin.
Step M must be finished before step V can begin.
Step I must be finished before step D can begin.
Step O must be finished before step P can begin."""
max_workers = 5
task_penalty = 60


# input = """Step C must be finished before step A can begin.
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

for line in input.splitlines():
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