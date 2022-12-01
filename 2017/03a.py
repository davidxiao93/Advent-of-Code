import file_loader

input_string = file_loader.get_input()

input_string = int(input_string)



if input_string == 1:
    print(0)
    exit()


n = 0
while True:
    if (2*n+1)*(2*n+1) + 1 <= input_string <= (2*n+3)*(2*n+3):
        break
    n += 1
distance_along_axis = n + 1

# bottom right corner = (2*n+3)*(2*n+3) ?
step = 2 * distance_along_axis

axis = [(2*n+1) * (2*n+1) + step*x for x in [0.5, 1.5, 2.5, 3.5]]

distance_to_axis = int(min([abs(input_string - x) for x in axis]))
# print(axis)
# print(distance_to_axis)
# print(distance_along_axis)

print(distance_to_axis + distance_along_axis)

