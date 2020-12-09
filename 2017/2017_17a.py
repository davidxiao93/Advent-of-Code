input = 301

# input = 3



buffer = [0]

def spinlock(s, n, q):
    n = n + 1
    n = n % len(s)
    s = [q] + s[n:] + s[:n]
    return s

for i in range(1, 2017 + 1):
    buffer = spinlock(buffer, input, i)

print(buffer[1])

