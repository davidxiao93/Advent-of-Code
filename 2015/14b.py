import file_loader

input_string = file_loader.get_input()

t = 2503

# input_string = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
# t = 1000

class Reindeer:
    def __init__(self, name, speed, flying_time, resting_time):
        self.distance_covered = 0
        self.current_time = 0
        self.is_flying = True
        self.time_since_last_change = 0
        self.points = 0
        self.name = name
        self.speed = speed
        self.flying_time = flying_time
        self.resting_time = resting_time

    def advance(self):
        self.current_time += 1
        self.time_since_last_change += 1
        if self.is_flying:
            self.distance_covered += self.speed
            if self.time_since_last_change >= self.flying_time:
                self.time_since_last_change = 0
                self.is_flying = False
        else:
            if self.time_since_last_change >= self.resting_time:
                self.time_since_last_change = 0
                self.is_flying = True
        # print(self.name,
        #       "is",
        #       "flying" if self.is_flying else "resting",
        #       "and has travelled",
        #       str(self.distance_covered),
        #       "after",
        #       str(self.current_time),
        #       "seconds"
        #       )

    def score_point(self):
        # print(self.name, "has scored a point")
        self.points += 1

reindeers = []
for line in input_string.split("\n"):
    words = line.split()
    name = words[0]
    speed = int(words[3])
    ft = int(words[6])
    rt = int(words[-2])

    reindeers.append(Reindeer(name, speed, ft, rt))


for i in range(t):
    for r in reindeers:
        r.advance()
    furthest = max([r.distance_covered for r in reindeers])
    for r in reindeers:
        if r.distance_covered == furthest:
            r.score_point()

print(max([r.points for r in reindeers]))

