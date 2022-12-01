import file_loader

input_string = file_loader.get_input()

t = 2503

# input_string = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
# t = 1000

import math

def distance_covered(speed, ft, rt, total_time):
    iterations = math.floor(total_time / (ft+rt))
    remaining = total_time % (ft + rt)
    return iterations * (ft * speed) + min(remaining, ft) * speed

furthest = 0
for line in input_string.split("\n"):
    words = line.split()
    speed = int(words[3])
    ft = int(words[6])
    rt = int(words[-2])

    distance = distance_covered(speed, ft, rt, t)
    if distance > furthest:
        furthest = distance

print(furthest)
