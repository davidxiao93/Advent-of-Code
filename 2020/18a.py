import file_loader

input_string = file_loader.get_input()


def evaluate(s):
    s = s.replace(" ", "")
    if len(s) == 0:
        return 0
    if s[-1] == ")":
        # find matching bracket and recurse
        nesting = 1
        index = None
        for i, c in enumerate(s[-2::-1]):
            if c == ")":
                nesting += 1
            elif c == "(":
                nesting -= 1
            if nesting == 0:
                index = len(s) - i - 3
                break
        if index == None:
            print("wtf, no matching bracket found")
        right = evaluate(s[index+2:-1])
        if index <= 0:
            # no more operators
            operator = None
            left = None
        else:
            operator = s[index]
            left = s[:index]
    else:
        index = len(s) - 1
        while index >= 0 and s[index] != "+" and s[index] != "*":
            index -= 1
        if index == -1:
            # no operator
            operator = None
            left = None
        else:
            operator = s[index]
            left = s[:index]
        right = int(s[index+1:])

    if operator == "+":
        return evaluate(left) + right
    elif operator == "*":
        return evaluate(left) * right
    else:
        return right

print(sum([
    evaluate(s)
    for s in input_string.splitlines()
]))