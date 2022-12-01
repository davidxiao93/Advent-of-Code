import file_loader

input_string = file_loader.get_input()


"""
observations:
the last digit after a FFT is only affected by the last digit before FFT
but it gos further than that
the last 2 digits after a FFT are only affected by the last 2 digits before FFT
and in general, the last k digits after FFT are only affected by the last k digits before FFT
    for k > n/2 where n is size of signal
Moreover, the pattern of the FFT for this second half is extremely simple:
    the kth last digit after FFT is the summation of the k last digits modulo 10 before FFT

then note, that the offset is 5977603. This is definitely within this realm of the second half
of the signal.
This greatly simplifies the required transform

"""

input_string = input_string * 10_000
offset = int(input_string[:7])

values = [int(c) for c in input_string][offset:]


for i in range(100):
    values = values[::-1]
    new_values = []
    acc = 0
    for v in values:
        acc += v
        new_values.append(acc)
    values = [abs(v) % 10 for v in new_values][::-1]

print("".join([str(x) for x in values[:8]]))
