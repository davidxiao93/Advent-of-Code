import file_loader

input_string = file_loader.get_input()

# input_string = """Begin in state A.
# Perform a diagnostic checksum after 6 steps.
#
# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state B.
#
# In state B:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A."""

config, *states_strings = input_string.split("\n\n")

def parse_state(state):
    """
    tuple: (name, what to write if 0, direction to move if 0, state to change to if 0,
                  what to write if 1, direction to move if 1, state to change to if 1)
    """
    lines = state.splitlines()
    name = lines[0].split()[-1][:-1]
    w0 = int(lines[2].split()[-1][:-1])
    d0 = -1 if lines[3].split()[-1][:-1] == "left" else 1
    s0 = lines[4].split()[-1][:-1]
    w1 = int(lines[6].split()[-1][:-1])
    d1 = -1 if lines[7].split()[-1][:-1] == "left" else 1
    s1 = lines[8].split()[-1][:-1]
    return (name, w0, d0, s0, w1, d1, s1)

starting_state = config.splitlines()[0].split()[-1][:-1]
diagnostic = int(config.splitlines()[1].split()[5])
states = {}
for s in states_strings:
    (name, w0, d0, s0, w1, d1, s1) = parse_state(s)
    states[name] = (w0, d0, s0, w1, d1, s1)

current_pos = 0
current_state = starting_state
tape = {}

def get_tape_value(pos):
    if pos not in tape:
        return 0
    else:
        return tape[pos]

def write_to_tape(pos, v):
    tape[pos] = v


for i in range(diagnostic):
    state = states[current_state]
    t = get_tape_value(current_pos)
    if t == 0:
        write_to_tape(current_pos, state[0])
        current_pos += state[1]
        current_state = state[2]
    else:
        write_to_tape(current_pos, state[3])
        current_pos += state[4]
        current_state = state[5]

def get_checksum(tape):
    return sum(tape.values())


print(get_checksum(tape))

