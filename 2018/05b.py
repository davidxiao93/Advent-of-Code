import file_loader

input_string = file_loader.get_input()



def reduce(input_string, units):
    changes_made = True
    while changes_made:
        changes_made = False
        for c in units:
            for duo in [c+c.upper(), c.upper()+c]:
                if duo in input_string:
                    changes_made = True
                    input_string = input_string.replace(duo, "")
    return input_string


units = set()
for c in input_string:
    units.add(c.lower())

shortest_len = None
for c in units:
    s = input_string.replace(c, "").replace(c.upper(), "")
    l = len(reduce(s, units))
    # print("removing", c, "allowed reduction to", l)
    if shortest_len is None or l < shortest_len:
        shortest_len = l

print(shortest_len)




