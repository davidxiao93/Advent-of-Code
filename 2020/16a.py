from typing import List, Dict

import file_loader

input_string = file_loader.get_input()

fields_str, my_ticket_str, other_tickets_str = input_string.split("\n\n")

fields: Dict[str, int] = dict()
for line in fields_str.splitlines():
    left, right = line.split(": ")
    right_a, right_b = right.split(" or ")
    values = [
        v
        for r in [right_a, right_b]
        for v in range(int(r.split("-")[0]), int(r.split("-")[1]))
    ]
    fields[left] = values

my_ticket = [int(x) for x in my_ticket_str.splitlines()[1].split(",")]

other_tickets = [
    [int(x) for x in other_ticket_str.split(",")]
    for other_ticket_str in other_tickets_str.splitlines()[1:]
]

def get_invalid_values(ticket: List[int], fields: Dict[str, int]):
    all_valid_values = set()
    invalid = 0
    for field, values in fields.items():
        all_valid_values |= set(values)
    for t in ticket:
        if t not in all_valid_values:
            invalid += t
    return invalid

error_rate = 0
for other_ticket in other_tickets:
    error_rate += get_invalid_values(other_ticket, fields)

print(error_rate)