import file_loader

input_string = file_loader.get_input()

target = 35651584



def dragon(a: str):
    return a + "0" + a[::-1].replace("0", "2").replace("1", "0").replace("2", "1")

def checksum(s: str):
    if len(s) % 2 == 1:
        return s
    result = "".join(["1" if len(set(s[i:i+2])) == 1 else "0" for i in range(0, len(s), 2)])
    return checksum(result)


while len(input_string) < target:
    input_string = dragon(input_string)

input_string = input_string[:target]

print(checksum(input_string))

