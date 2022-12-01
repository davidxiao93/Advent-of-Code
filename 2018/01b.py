import file_loader

input_string = file_loader.get_input()


seen_frequencies = { 0 }
current_frequency = 0
current_instruction = 0
instructions = input_string.splitlines()
seen = False
duplicate_frequency = None
while not seen:
    instruction = instructions[current_instruction]
    current_frequency += int(instruction)
    if current_frequency in seen_frequencies:
        seen = True
        duplicate_frequency = current_frequency
        break
    seen_frequencies.add(current_frequency)
    current_instruction = (current_instruction + 1) % len(instructions)

print(duplicate_frequency)