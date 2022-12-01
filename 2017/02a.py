import file_loader

input_string = file_loader.get_input()


checksum = 0
for line in input_string.splitlines():
    values = { int(x) for x in line.split() }
    checksum += max(values)
    checksum -= min(values)

print(checksum)