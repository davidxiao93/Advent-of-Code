input = """192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"""
input = [int(x) for x in input.split(",")]
num = 256


# input = [3, 4, 1, 5]
# num = 5



def shift_left(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

def reverse(s, n):
    r = s[:n]
    r = r[::-1]
    return r + s[n:]


s = []
for i in range(num):
    s.append(i)

current_pos = 0
skip_size = 0
for i in input:
    s = reverse(s, i)
    s = shift_left(s, i + skip_size)
    current_pos = ((current_pos - i) - skip_size) % len(s)
    skip_size += 1
final_s = s[current_pos:] + s[:current_pos]

print(final_s[0] * final_s[1])


