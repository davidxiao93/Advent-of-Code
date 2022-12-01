import file_loader

input_string = file_loader.get_input()

score = 0

is_in_garbage = False
nesting = 1
while len(input_string) != 0:
    c = input_string[0]
    if c == "{":
        if not is_in_garbage:
            score += nesting
            nesting += 1
        input_string = input_string[1:]
    elif c == "}":
        if not is_in_garbage:
            nesting -= 1
        input_string = input_string[1:]
    elif c == "!":
        if is_in_garbage:
            input_string = input_string[2:]
        else:
            print("wtf")
            exit(1)
    elif c == "<":
        if not is_in_garbage:
            is_in_garbage = True
        input_string = input_string[1:]
    elif c == ">":
        if is_in_garbage:
            is_in_garbage = False
        input_string = input_string[1:]
    else:
        input_string = input_string[1:]

print(score)



