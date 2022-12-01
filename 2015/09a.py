import file_loader

input_string = file_loader.get_input()

best_path = 2147483647
mapping = {}
nodes = set()


def visit_next(current_path_length, last, unvisited):
    global best_path
    if current_path_length > best_path:
        return
    if len(unvisited) == 0:
        if current_path_length < best_path:
            best_path = current_path_length
        return

    for next in unvisited:
        visit_next(
            current_path_length + mapping[(last, next)],
            next,
            { u for u in unvisited if u != next }
        )


def visit_first(start):
    unvisited = { u for u in nodes if u != start }
    visit_next(0, start, unvisited)


for line in input_string.split("\n"):
    direction, dist = line.split("=")
    a, b = direction.split("to")
    mapping[(a.strip(), b.strip())] = int(dist.strip())
    mapping[(b.strip(), a.strip())] = int(dist.strip())
    nodes.add(a.strip())
    nodes.add(b.strip())

for node in nodes:
    visit_first(node)

print(best_path)