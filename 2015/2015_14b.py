input = """Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."""
t = 2503

# input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
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
        print(self.name,
              "is",
              "flying" if self.is_flying else "resting",
              "and has travelled",
              str(self.distance_covered),
              "after",
              str(self.current_time),
              "seconds"
              )

    def score_point(self):
        print(self.name, "has scored a point")
        self.points += 1

reindeers = []
for line in input.split("\n"):
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

print(sorted([r.points for r in reindeers]))

