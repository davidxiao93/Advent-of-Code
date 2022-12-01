import file_loader

input_string = file_loader.get_input()

from datetime import datetime, timedelta

guard_mapping = {}

current_guard_id = None
current_shift_minute = 0
for line in sorted(input_string.splitlines()):
    l, r = line.split("]")
    date = datetime.strptime(l[1:11], "%Y-%m-%d")
    hour = int(l[12:14])
    minute = int(l[15:17])
    if hour == 1:
        minute = 60
    if hour == 23:
        date += timedelta(days=1)
        minute = 0
    if "#" in line:
        current_guard_id = int(r.split()[1][1:])
        if current_guard_id not in guard_mapping:
            guard_mapping[current_guard_id] = {}
        guard_mapping[current_guard_id][date] = [0] * 60
        current_shift_minute = 0
    elif "wakes up" in line:
        for i in range(current_shift_minute, minute):
            guard_mapping[current_guard_id][date][i] = 1
        current_shift_minute = minute
    elif "falls asleep" in line:
        for i in range(current_shift_minute, minute):
            guard_mapping[current_guard_id][date][i] = 0
        current_shift_minute = minute
    else:
        print("wft")
        exit(0)


frequently_asleep = max([
    ((guard_id,) + max(enumerate([
        sum(z) for z in zip(*date_mapping.values())
    ]), key=lambda k: k[-1]))
    for guard_id, date_mapping in guard_mapping.items()
], key=lambda k: k[-1])

print(frequently_asleep[0] * frequently_asleep[1])
