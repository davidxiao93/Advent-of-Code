import file_loader

input_string = file_loader.get_input()

# input_string = "A(1x5)BC"
# input_string = "A(2x2)BCD(2x2)EFG"
# input_string = "(6x1)(1x3)A"
# input_string = "X(8x2)(3x3)ABCY"
# input_string = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
# input_string = "(27x12)(20x12)(13x14)(7x10)(1x12)A"

def size_of_decompression(s):
    count = 0
    if len(s) == 0:
        return count
    while s[0] != '(':
        count += 1
        s = s[1:]
        if len(s) == 0:
            return count

    s = s[1:]  # remove initial bracket
    marker = ""
    while s[0] != ')':
        marker += s[0]
        s = s[1:]
    s = s[1:]  # remove second bracket

    number_chars_to_repeat, repeat_times = [int(x) for x in marker.split("x")]
    chars_to_repeat = s[:number_chars_to_repeat]
    remaining = s[number_chars_to_repeat:]
    return count + repeat_times * size_of_decompression(chars_to_repeat) + size_of_decompression(remaining)



print(size_of_decompression(input_string))




