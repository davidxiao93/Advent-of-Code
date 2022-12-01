import file_loader

input_string = file_loader.get_input()
input_string = [int(i) for i in input_string.split(",")]

lowest_score = -1
for i in range(min(input_string), max(input_string) + 1):
    score = 0
    for v in input_string:
        score += abs(v - i)
    if lowest_score < 0 or score < lowest_score:
        lowest_score = score

print(lowest_score)