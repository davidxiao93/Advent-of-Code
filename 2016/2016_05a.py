import hashlib

input = """wtnhxymk"""


def hash(key, n):
    return hashlib.md5((key + str(n)).encode('utf-8')).hexdigest()

index = 0
password = ""
while len(password) != 8:
    h = hash(input, index)
    if h.startswith("00000"):
        password += h[5]
    index += 1

print(password)