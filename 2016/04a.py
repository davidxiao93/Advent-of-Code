import file_loader

input_string = file_loader.get_input()

def is_real(s):
    # returns id if real, 0 otherwise
    ni, c = s.split("[")
    checksum = c[:-1]
    ni_rs = ni.rsplit("-", 1)
    e_name = ni_rs[0].replace("-", "")
    id = int(ni_rs[1])

    counts = {}
    for c in e_name:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    counts_to_c = {}
    for char, count in counts.items():
        if count not in counts_to_c:
            counts_to_c[count] = []
        counts_to_c[count].append(char)

    calc_checksum = ""
    while len(calc_checksum) < 5:
        key = max(counts_to_c)
        calc_checksum += "".join(sorted(counts_to_c[key]))
        counts_to_c.pop(key, None)

    calc_checksum = calc_checksum[:5]
    if calc_checksum != checksum:
        return 0

    return id


# print(is_real("totally-real-room-200[decoy]"))
#
# exit()

total = 0
for line in input_string.splitlines():
    total += is_real(line)


print(total)
