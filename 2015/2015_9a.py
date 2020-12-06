input = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""

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


for line in input.split("\n"):
    direction, dist = line.split("=")
    a, b = direction.split("to")
    mapping[(a.strip(), b.strip())] = int(dist.strip())
    mapping[(b.strip(), a.strip())] = int(dist.strip())
    nodes.add(a.strip())
    nodes.add(b.strip())

for node in nodes:
    visit_first(node)

print(best_path)