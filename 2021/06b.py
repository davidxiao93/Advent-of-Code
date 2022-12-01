import file_loader

input_string = file_loader.get_input()
input_string = [int(i) for i in input_string.split(",")]

NUM_DAYS = 256

spawns_on_day = {
    0: 1
}

for i in range(NUM_DAYS + 10):
    if i == 7:
        continue
    new_spawns = spawns_on_day.get(i-9, 0) + spawns_on_day.get(i-7, 0)
    if new_spawns != 0:
        spawns_on_day[i] = new_spawns


def get_fish_num(s: int) -> int:
    """
    returns number of fish spawned from a single fish after NUM_DAYS days given its starting age
    """
    return sum([v for k, v in spawns_on_day.items() if k < NUM_DAYS + 9 - s])

print(sum([
    get_fish_num(s)
    for s in input_string
]))


