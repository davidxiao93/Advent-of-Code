import hashlib

import file_loader

input_string = file_loader.get_input()

def success(number):
    return hashlib.md5((input_string + str(number)).encode('utf-8')).hexdigest().startswith("00000")

i = 0
while not success(i):
    i += 1

print(i)