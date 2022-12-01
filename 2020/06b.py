import file_loader

input_string = file_loader.get_input()

# input_string = """abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b"""

count = 0
for group in input_string.split("\n\n"):
    answers = {}
    for person in group.splitlines():
        for answer in person:
            if answer not in answers:
                answers[answer] = 0
            answers[answer] += 1
    for answer, num in answers.items():
        count += 1 if num == len(group.splitlines()) else 0

print(count)