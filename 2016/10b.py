import file_loader

input_string = file_loader.get_input()


# input_string = """value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2"""

bot_comparisons = {}
bot_contents = {}
output_contents = {}

def get_output_location(s):
    if s[0] == "output":
        contents = output_contents
    elif s[0] == "bot":
        contents = bot_contents
    else:
        print("unknown contents")
        exit(1)

    n = int(s[1])
    if n not in contents:
        contents[n] = []
    return contents[n]


value_instructions = []
bot_instructions = {}

for line in input_string.splitlines():
    if line.startswith("value"):
        value_instructions.append(line)
    else:
        words = line.split()
        bn = int(words[1])
        if bn in bot_instructions:
            print("should a bot have multiple instrucitons?")
            exit(1)
        bot_instructions[bn] = line


def process_bot(bn):
    if bn not in bot_instructions:
        print("unknown instruction")
        exit(1)
    words = bot_instructions[bn].split()
    bn = int(words[1])
    lower_o = words[5:7]
    higher_o = words[-2:]
    bot_content = bot_contents[bn]
    if len(bot_content) > 2:
        print("wrong length for comparison")
        exit(1)
    if len(bot_content) < 2:
        # do nothing
        return
    bot_content.sort()

    if lower_o[0] == "output":
        give_output_bin_chip(int(lower_o[1]), bot_content[0])
    else:
        give_bot_chip(int(lower_o[1]), bot_content[0])

    if higher_o[0] == "output":
        give_output_bin_chip(int(higher_o[1]), bot_content[1])
    else:
        give_bot_chip(int(higher_o[1]), bot_content[1])

    comparison = (bot_content[0], bot_content[1])
    if comparison not in bot_comparisons:
        bot_comparisons[comparison] = []
    bot_comparisons[comparison].append(bn)
    bot_contents[bn] = []


def give_bot_chip(bn, v):
    if bn not in bot_contents:
        bot_contents[bn] = []
    bot_contents[bn].append(v)
    process_bot(bn)


def give_output_bin_chip(on, v):
    if on not in output_contents:
        output_contents[on] = []
    output_contents[on].append(v)


for value_instruction in value_instructions:
    words = value_instruction.split()
    v = int(words[1])
    bn = int(words[-1])
    give_bot_chip(bn, v)


print(output_contents[0][0] * output_contents[1][0] * output_contents[2][0])


