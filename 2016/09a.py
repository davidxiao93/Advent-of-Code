import file_loader

input_string = file_loader.get_input()

# input_string = "A(1x5)BC"
# input_string = "A(2x2)BCD(2x2)EFG"
# input_string = "(6x1)(1x3)A"
# input_string = "X(8x2)(3x3)ABCY"

def decompressish(s):
    """
    returns tuple (X, S) where X is the size of the decompressed parts,
                        and S is the remaining string to decompress
    """
    count = 0
    while s[0] != '(':
        count += 1
        s = s[1:]
        if len(s) == 0:
            return (count, "")

    s = s[1:] # remove initial bracket
    marker = ""
    while s[0] != ')':
        marker += s[0]
        s = s[1:]
    s = s[1:] # remove second bracket

    number_chars_to_repeat, repeat_times = [int(x) for x in marker.split("x")]

    chars_to_repeat = s[:number_chars_to_repeat]
    remaining = s[number_chars_to_repeat:]
    # print(count, chars_to_repeat, repeat_times, remaining)

    return (count + len(chars_to_repeat) * repeat_times, remaining)


total_count = 0
remaining = input_string
while len(remaining) != 0:
    c, r = decompressish(remaining)
    total_count += c
    remaining = r

print(total_count)






