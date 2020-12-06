input = """00101000101111010"""

target = 35651584



def dragon(a: str):
    return a + "0" + a[::-1].replace("0", "2").replace("1", "0").replace("2", "1")

def checksum(s: str):
    if len(s) % 2 == 1:
        return s
    result = "".join(["1" if len(set(s[i:i+2])) == 1 else "0" for i in range(0, len(s), 2)])
    return checksum(result)


while len(input) < target:
    print(len(input))
    input = dragon(input)

input = input[:target]

print(checksum(input))

