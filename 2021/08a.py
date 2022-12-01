import file_loader

input_string = file_loader.get_input()

count = 0

for line in input_string.splitlines():
    signals = line.split("|")[0].strip().split(" ")
    outputs = line.split("|")[1].strip().split(" ")

    count += sum([1 for x in outputs if len(x.strip()) in {2, 4, 3, 7}])

print(count)
