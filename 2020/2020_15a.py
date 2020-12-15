input = """19,0,5,1,10,13"""
target = 2020


values = [int(x) for x in input.split(",")]

last_number = values[-1]
last_seen = {}
turns_played = len(values)
for i in range(len(values) - 1):
    last_seen[values[i]] = i + 1

while turns_played < target:
    if last_number not in last_seen:
        next_number = 0
    else:
        next_number = turns_played - last_seen[last_number]
    last_seen[last_number] = turns_played
    last_number = next_number
    turns_played += 1

print(last_number)
