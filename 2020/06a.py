import file_loader

input_string = file_loader.get_input()


count = 0
for group in input_string.split("\n\n"):
    answers = set()
    for person in group.splitlines():
        for answer in person:
            answers.add(answer)
    count += len(answers)

print(count)