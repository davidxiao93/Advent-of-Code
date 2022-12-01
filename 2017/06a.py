import file_loader

input_string = file_loader.get_input()

# input_string = """0 2 7 0"""

banks = (int(x) for x in input_string.split())

def redistribute(b):
    bs = list(b)
    largest = 0
    largest_index = 0
    for i, m in enumerate(bs):
        if m > largest:
            largest = m
            largest_index = i

    i = (largest_index + 1)%len(bs)
    bs[largest_index] = 0
    for _ in range(largest):
        bs[i] += 1
        i = (i + 1) % len(bs)
    return tuple(bs)


seen_states = { banks }
current_state = banks
counter = 0
while True:
    counter += 1
    new_banks = redistribute(banks)
    banks = new_banks
    if new_banks in seen_states:
        print(counter)
        break
    seen_states.add(new_banks)

