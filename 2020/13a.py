input = """1003055
37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,433,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,29,x,593,x,x,x,x,x,x,x,x,x,x,x,x,13"""


offset = int(input.splitlines()[0])
buses = [int(x) for x in input.splitlines()[1].split(",") if x != "x"]

minutes_waited = 1
while True:
    for b in buses:
        if (offset + minutes_waited) % b == 0:
            print(b * minutes_waited)
            exit(0)


    minutes_waited += 1

