import file_loader

input_string = file_loader.get_input()


offset = int(input_string.splitlines()[0])
buses = [int(x) for x in input_string.splitlines()[1].split(",") if x != "x"]

minutes_waited = 1
while True:
    for b in buses:
        if (offset + minutes_waited) % b == 0:
            print(b * minutes_waited)
            exit(0)


    minutes_waited += 1

