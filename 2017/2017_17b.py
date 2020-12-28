input = """301"""
input = int(input)

"""
After playing around with spinlock for a bit, not that the only time the value after 0 is changed
We do not actually need to perform the entire spinlock, we only need to keep track of where the 
zero is, and what the value is after it

Because the implementation of spinlock in part a always has the newly inserted value at the front, 
then we only need to check if the zero is at the end

buffer, zero_index:
[0] 0
[1, 0] 1
[2, 1, 0] 2
[3, 1, 0, 2] 2
[4, 3, 1, 0, 2] 3
[5, 2, 4, 3, 1, 0] 5
[6, 1, 0, 5, 2, 4, 3] 2
[7, 2, 4, 3, 6, 1, 0, 5] 6
[8, 6, 1, 0, 5, 7, 2, 4, 3] 3
[9, 5, 7, 2, 4, 3, 8, 6, 1, 0] 9
[10, 4, 3, 8, 6, 1, 0, 9, 5, 7, 2] 6
[11, 6, 1, 0, 9, 5, 7, 2, 10, 4, 3, 8] 3
[12, 9, 5, 7, 2, 10, 4, 3, 8, 11, 6, 1, 0] 12

so the value after 0 changes when the newly inserted value is equal to the zero_index
namely, at 0, 1, 5, 9 and 12

We can in fact completely forgo the spinlock implementation, and calculate the zero_indexes directly.

"""

zero_index = 0

after_zero = 0
i = 1
target = 50000000
while i <= target:

    zero_index = 1 + ((zero_index - 1 - input) % i)
    # print(i, "\t", zero_index, "----" if i == zero_index else "")
    if i == zero_index:
        after_zero = i

    # If our zero index is high, then we can skip ahead
    if zero_index > 2*input:
        i += (zero_index // input) - 1
        zero_index = (zero_index % input) + input
        i += 1
    else:
        i += 1

print(after_zero)


