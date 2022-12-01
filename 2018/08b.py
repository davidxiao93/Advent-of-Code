import file_loader

input_string = file_loader.get_input()
values = tuple([int(x) for x in input_string.split()])


def get_child(v):
    num_children = v[0]
    num_metadata = v[1]
    if num_children == 0:
        return v[2:2 + num_metadata], v[2+num_metadata:]
    # has children
    remaining_nodes = v[2:]
    seen_children = 0
    children = tuple()
    while seen_children != num_children:
        child, remaining_nodes = get_child(remaining_nodes)
        children += (child,)
        seen_children += 1
    return children + remaining_nodes[:num_metadata], remaining_nodes[num_metadata:]

def get_root(v):
    return get_child(v)[0]

def score_node(r):
    ts = []
    ms = []
    for i in range(len(r)):
        if isinstance(r[i], tuple):
            ts.append(r[i])
        else:
            ms.append(r[i] - 1)
    if len(ts) == 0:
        # no children
        # add on len(ms) because of r[i] - 1
        return sum(ms) + len(ms)
    score = 0
    for m in ms:
        if 0 <= m < len(ts):
            score += score_node(ts[m])

    return score

print(score_node(get_root(values)))


