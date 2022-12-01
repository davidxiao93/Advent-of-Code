import file_loader

input_string = file_loader.get_input()

seat_ids = []
for line in input_string.splitlines():
    seat_binary = line.replace("L", "0").replace("R", "1").replace("F", "0").replace("B", "1")
    seat_id = int(seat_binary, 2)
    seat_ids.append(seat_id)

seat_ids = sorted(seat_ids)

seat_ids = [s for s in seat_ids if 8 <= s < 127*8]

for a, b in zip(seat_ids, seat_ids[1:]):
    if b - a == 2:
        print(a + 1)