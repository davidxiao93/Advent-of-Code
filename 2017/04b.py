import file_loader

input_string = file_loader.get_input()

count = 0
for line in input_string.splitlines():
    words = line.split()
    words = ["".join(sorted(list(w))) for w in words]
    if len(words) == len(set(words)):
        count += 1

print(count)