import file_loader

input_string = file_loader.get_input()

points = []
folds = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fold(self, axis, pos):
        if axis == "y":
            # folding upwards
            if self.y > pos:
                self.y = 2*pos - self.y
        elif axis == "x":
            # folding leftwards
            if self.x > pos:
                self.x = 2*pos - self.x
        else:
            raise Exception("unknown axis")

for line in input_string.splitlines():
    if len(line) == 0:
        continue
    if line.startswith("f"):
        folds.append((
            line.split()[2].split("=")[0],
            int(line.split()[2].split("=")[1])
        ))
    else:
        points.append(Point(
            int(line.split(",")[0]),
            int(line.split(",")[1])
        ))

for f in folds:
    for p in points:
        p.fold(f[0], f[1])

remaining_points = {
    (p.x, p.y) for p in points
}
max_x = max([p.x for p in points])
max_y = max([p.y for p in points])

for y in range(max_y + 1):
    for x in range(max_x + 1):
        if (x, y) in remaining_points:
            print("#", end="")
        else:
            print(".", end="")
    print("")
