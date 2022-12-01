import file_loader

input_string = file_loader.get_input()


def can_reduce(a:str, b:str):
    return ((a.islower() and b.isupper()) or (a.isupper() and b.islower())) and a.lower() == b.lower()


changes_made = True
while changes_made:
    changes_made = False
    i = 0
    while 0 <= i and i + 1 < len(input_string):
        if can_reduce(input_string[i], input_string[i+1]):
            input_string = input_string[:i] + input_string[i+2:]
            changes_made = True
        i += 1

print(len(input_string))


