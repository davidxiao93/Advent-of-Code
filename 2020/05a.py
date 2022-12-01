import file_loader

input_string = file_loader.get_input()

max_seat_id = 0
for line in input_string.splitlines():
    seat_binary = line.replace("L", "0").replace("R", "1").replace("F", "0").replace("B", "1")
    seat_id = int(seat_binary, 2)
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)