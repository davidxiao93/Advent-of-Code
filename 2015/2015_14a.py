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

import math

def distance_covered(speed, ft, rt, total_time):
    iterations = math.floor(total_time / (ft+rt))
    remaining = total_time % (ft + rt)
    return iterations * (ft * speed) + min(remaining, ft) * speed

furthest = 0
for line in input.split("\n"):
    words = line.split()
    speed = int(words[3])
    ft = int(words[6])
    rt = int(words[-2])

    distance = distance_covered(speed, ft, rt, t)
    if distance > furthest:
        furthest = distance

print(furthest)
