import file_loader

input_string = file_loader.get_input()
input_string = [int(i) for i in input_string.split(",")]

fish = [0]
num_fish = {
    0: 1
}
for i in range(80):
    new_fish = []
    for f in fish:
        if f == 0:
            new_fish.append(6)
            new_fish.append(8)
        else:
            new_fish.append(f-1)
    num_fish[i+1] = len(new_fish)
    fish = new_fish

def get_fish_num(s: int) -> int:
    """
    returns number of fish spawned from a single fish after 80 days given its starting age
    """
    return num_fish[80-s]

print(sum([
    get_fish_num(s)
    for s in input_string
]))