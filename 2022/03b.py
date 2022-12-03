import file_loader

input_string = file_loader.get_input()

s = 0
iterator = iter(input_string.splitlines())
for line1 in iterator:
    line2 = next(iterator)
    line3 = next(iterator)
    x = set(line1).intersection(set(line2)).intersection(set(line3)).pop()
    s += ord(x) - (96 if x.islower() else 38)

print(s)