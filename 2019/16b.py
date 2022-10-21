input = """59776034095811644545367793179989602140948714406234694972894485066523525742503986771912019032922788494900655855458086979764617375580802558963587025784918882219610831940992399201782385674223284411499237619800193879768668210162176394607502218602633153772062973149533650562554942574593878073238232563649673858167635378695190356159796342204759393156294658366279922734213385144895116649768185966866202413314939692174223210484933678866478944104978890019728562001417746656699281992028356004888860103805472866615243544781377748654471750560830099048747570925902575765054898899512303917159138097375338444610809891667094051108359134017128028174230720398965960712"""


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

input = input * 10_000
offset = int(input[:7])

values = [int(c) for c in input][offset:]


for i in range(100):
    values = values[::-1]
    new_values = []
    acc = 0
    for v in values:
        acc += v
        new_values.append(acc)
    values = [abs(v) % 10 for v in new_values][::-1]

print("".join([str(x) for x in values[:8]]))
