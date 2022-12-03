import file_loader

input_string = file_loader.get_input()

print(sum([
    ord(x) - (96 if x.islower() else 38)
    for x in  [
        set(line[:int(len(line)/2)]).intersection(set(line[int(len(line)/2):])).pop()
        for line in input_string.splitlines()
    ]
]))
