input = """477 players; last marble is worth 70851 points"""

words = input.split()
highest_marble = int(words[-2]) * 100 # Part 2
num_players = int(words[0])


def shift(v, a):
    if a != 0 and a % 23 == 0:
        return v[-6:] + v[:-7], {v[-7], a}
    else:
        return [a] + v[2:] + v[:2], set()


def shift_faster(v, m):
    # m should be of the form 23*n + 1 for some integer n
    r = v[:2]
    for i, m in enumerate(range(m, m + 22)):
        r.append(m)
        r.append(v[i+2])
    r += v[24:]
    return r[38:] + r[:37], {r[37], m + 1}


def shift_even_faster(v, m, highest_marble):
    # m should be of the form 23*n + 1 for some integer n
    # returns new_v, next_m, score_dict
    rows = [v[1:19]]
    v = v[19:] + [v[0]]
    score_dict = {}
    counter = 0
    # This 80 is a magic number, it just needs to be large enough to not mess up the end of the list
    # but theres probably a special case where some missing scores would happen
    while len(v) > 80:
        counter += 1
        processed_marble = (m - 1 + counter*23)
        print(processed_marble)
        if processed_marble > highest_marble:
            return [], 0, score_dict
        elf = processed_marble % num_players
        if elf not in score_dict:
            score_dict[elf] = 0
        score_dict[elf] += v[0] + processed_marble
        rows.append(v[1:16])
        v = v[16:]
    processed_marble = (m - 1 + (counter + 1) * 23)
    print(processed_marble)
    if processed_marble > highest_marble:
        return [], 0, score_dict
    elf = processed_marble % num_players
    if elf not in score_dict:
        score_dict[elf] = 0
    score_dict[elf] += v[0]  + processed_marble
    rows.append(v[1:])
    for i in range(1, len(rows)):
        rows[i] = [rows[i][0], rows[0][1] + i*23, rows[i][1], rows[0][1] + i*23 + 1, rows[i][2], rows[0][1] + i*23 + 2] + rows[i][3:]

    for i in range(0, len(rows) - 1):
        new_row = []
        for x, v in enumerate(rows[i]):
            new_row.append(v)
            new_row.append(rows[i][1] + 4 + x)
        new_row.append(rows[i][1] + 22)
        rows[i] = new_row

    rows = [rows[-1]] + rows[:-1]
    v = sum(rows, [])
    v = [v[-1]] + v[:-1]
    next_marble = (m - 1 + (counter + 1)*23) + 1
    return v, next_marble, score_dict








elf_scores = {}
values = [0]
marble = 1
while marble <= highest_marble:
    print(marble)
    if marble <= 2*23:
        values, removed = shift(values, marble)
        if len(removed) > 0:
            elf = ((marble - 1) % num_players) + 1
            if elf not in elf_scores:
                elf_scores[elf] = 0
            elf_scores[elf] += sum(removed)
        marble += 1
    elif marble <= 10*23:
        values, removed = shift_faster(values, marble)
        if len(removed) > 0:
            elf = ((marble + 22) % num_players)
            if elf not in elf_scores:
                elf_scores[elf] = 0
            elf_scores[elf] += sum(removed)
        marble += 23
    else:
        values, marble, new_scores = shift_even_faster(values, marble, highest_marble)
        for elf, score in new_scores.items():
            if elf not in elf_scores:
                elf_scores[elf] = 0
            elf_scores[elf] += score



print(max(elf_scores.values()))