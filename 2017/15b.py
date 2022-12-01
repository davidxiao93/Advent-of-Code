import file_loader

input_string = file_loader.get_input()

inputA = int(input_string.splitlines()[0].split()[-1])
inputB = int(input_string.splitlines()[1].split()[-1])

# inputA = 65
# inputB = 8921

factorA = 16807
factorB = 48271

bound = 2147483647

def generate_next(prev, factor):
    return (prev * factor) % bound

a = inputA
b = inputB
matches = 0
for i in range(5000000):
    a = generate_next(a, factorA)
    while a % 4  != 0:
        a = generate_next(a, factorA)
    b = generate_next(b, factorB)
    while b % 8 != 0:
        b = generate_next(b, factorB)
    # bottom 16 bits match if they ae equal modulo 65536 (2^16)
    if (a % 65536) == (b % 65536):
        matches += 1

print(matches)


