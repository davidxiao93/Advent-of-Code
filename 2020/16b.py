from typing import List, Dict, Set

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
        for v in range(int(r.split("-")[0]), int(r.split("-")[1]) + 1)
    ]
    fields[left] = values

my_ticket = [int(x) for x in my_ticket_str.splitlines()[1].split(",")]

other_tickets = [
    [int(x) for x in other_ticket_str.split(",")]
    for other_ticket_str in other_tickets_str.splitlines()[1:]
]

def is_valid(ticket: List[int], fields: Dict[str, int]):
    all_valid_values = set()
    for field, values in fields.items():
        all_valid_values |= set(values)
    for t in ticket:
        if t not in all_valid_values:
            return False
    return True

valid_tickets = []
for other_ticket in other_tickets:
    if is_valid(other_ticket, fields):
        valid_tickets.append(other_ticket)

def get_potential_fields(f, fields):
    possible_fields = set()
    for field, values in fields.items():
        if f in values:
            possible_fields.add(field)
    return possible_fields

candidate_mapping: Dict[int, Set[str]] = {}
for valid_ticket in valid_tickets:
    for i, v in enumerate(valid_ticket):
        possible_fields = get_potential_fields(v, fields)
        if i not in candidate_mapping:
            candidate_mapping[i] = possible_fields
        else:
            candidate_mapping[i] &= possible_fields

field_to_position = {}
while len(candidate_mapping) > 0:
    candidates_to_clear_out = set()
    for position, candidates in candidate_mapping.items():
        if len(candidates) == 1:
            found_candidate = candidates.pop()
            candidates_to_clear_out.add(found_candidate)
            field_to_position[found_candidate] = position
    finalised_positions = set()
    for c in candidates_to_clear_out:
        for position, candidates in candidate_mapping.items():
            if c in candidates:
                candidates.remove(c)
            if len(candidates) == 0:
                finalised_positions.add(position)
    for p in finalised_positions:
        candidate_mapping.pop(p, None)


interested_fields = {
    field: position
    for field, position in field_to_position.items()
    if field.startswith("departure")
}

answer = 1
for field, position in interested_fields.items():
    answer *= my_ticket[position]

print(answer)



