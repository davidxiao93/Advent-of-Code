import file_loader

input_string = file_loader.get_input()

public_keys = [int(x) for x in input_string.splitlines()]

def transform(subject_number, loop_size):
    result = 1
    for i in range(loop_size):
        result = (result * subject_number) % 20201227
    return result

def get_loop_size(public_key):
    inverses = {}
    for i in range(7):
        inverse = 0
        v = i
        while (v + inverse) % 7 != 0:
            inverse += 20201227
        inverses[i] = inverse
    count = 0
    v = public_key
    while v != 1:
        v += inverses[v%7]
        count += 1
        v = v / 7
    loop_size = count
    assert(transform(7, loop_size) == public_key)
    return loop_size

# public_keys = [5764801, 17807724]

encryption_key = transform(public_keys[1], get_loop_size(public_keys[0]))
print(encryption_key)