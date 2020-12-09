inputA = 618
inputB = 814

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
for i in range(40000000):
    print(i)
    a = generate_next(a, factorA)
    b = generate_next(b, factorB)
    # bottom 16 bits match if they ae equal modulo 65536 (2^16)
    if (a % 65536) == (b % 65536):
        matches += 1

print(matches)


