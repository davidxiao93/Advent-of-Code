import file_loader

input_string = file_loader.get_input()

values = {}
mapping = {}

for line in input_string.split("\n"):
    destination = line.split("->")[-1].strip()
    provider = line.split("->")[0].strip()

    mapping[destination] = provider


# evaluate for a

def evaluate(target):

    if target.isnumeric():
        return int(target)

    if target in values:
        return values[target]

    if target not in mapping:
        print("Unknown target", target)
        exit(1)

    target_provider = mapping[target]

    args = target_provider.split()
    if len(args) == 1:
        # Assignment
        values[target] = evaluate(args[0])
    elif len(args) == 2:
        # NOT
        values[target] = ~evaluate(args[1])
    else:
        if args[1] == "AND":
            values[target] = evaluate(args[0]) & evaluate(args[2])
        elif args[1] == "OR":
            values[target] = evaluate(args[0]) | evaluate(args[2])
        elif args[1] == "LSHIFT":
            values[target] = evaluate(args[0]) << evaluate(args[2])
        elif args[1] == "RSHIFT":
            values[target] = evaluate(args[0]) >> evaluate(args[2])
        else:
            print("unknown operator", args[1])
            exit(1)

    if target not in values:
        print("How did i get here")
        exit(1)

    return values[target]


a = evaluate("a")

values = {}
values["b"] = a

print(evaluate("a"))



