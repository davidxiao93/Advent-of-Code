import hashlib

input = """yzbqklnj"""

def success(number):
    return hashlib.md5((input + str(number)).encode('utf-8')).hexdigest().startswith("000000")

i = 0
while not success(i):
    i += 1

print(i)