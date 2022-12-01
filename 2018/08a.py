import file_loader

input_string = file_loader.get_input()
values = tuple([int(x) for x in input_string.split()])


def get_sum(v):
    num_children = v[0]
    num_metadata = v[1]
    if num_children == 0:
        return sum(v[2:2 + num_metadata]), v[2+num_metadata:]
    # has children
    remaining_nodes = v[2:]
    seen_children = 0
    children = 0
    while seen_children != num_children:
        child_sum, remaining_nodes = get_sum(remaining_nodes)
        children += child_sum
        seen_children += 1
    return children + sum(remaining_nodes[:num_metadata]), remaining_nodes[num_metadata:]


print(get_sum(values)[0])



