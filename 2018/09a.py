import file_loader

input_string = file_loader.get_input()

words = input_string.split()
highest_marble = int(words[-2])
num_players = int(words[0])


def shift(v, a):
    if a != 0 and a % 23 == 0:
        return v[-6:] + v[:-7], {v[-7], a}
    else:
        return [a] + v[2:] + v[:2], set()

values = [0]
elf_scores = {}
for i in range(1, highest_marble + 1):
    values, removed = shift(values, i)
    elf = ((i - 1) % num_players) + 1
    if elf not in elf_scores:
        elf_scores[elf] = 0
    elf_scores[elf] += sum(removed)

print(max(elf_scores.values()))

