import file_loader

input_string = file_loader.get_input()
# TODO: this needs to be redone

"""

    00 cpy a d
    01 cpy 14 c
07
    02 cpy 182 b
05
    03 inc d
    04 dec b
    05 jnz b -2
    06 dec c
    07 jnz c -5
    # Steps 02 - 07 is:
        r = register before step 02
        nr = register after step 07
        nr[b] = 0
        nr[c] = 0
        nr[d] = r[d] + 182 * r[c]
        next_instruction = 08


29
    08 cpy d a




28
    09 jnz 0 0  # Does nothing
    10 cpy a b
    11 cpy 0 a



19
    12 cpy 2 c
17
    13 jnz b 2
    14 jnz 1 6
13
    15 dec b
    16 dec c
    17 jnz c -4
    18 inc a
    19 jnz 1 -7
    # Steps 12 - 19 is:
        r = register before step 12
        nr = register after step 14
        nr[a] = math.floor(r[b]/2)
        nr[b] = 0
        nr[c] = 2 if r[b] is even, otherwise 1
        next_instruction = 20


14
    20 cpy 2 b



25
    21 jnz c 2
    22 jnz 1 4
21
    23 dec b
    24 dec c
    25 jnz 1 -4
    # Steps 21 - 25 is:
        r = register before step 21
        nr = register after step 22
        nr[b] = r[b] - r[c]
        nr[c] = 0
        next_instruction = 26



22
    26 jnz 0 0  # Does nothing
    27 out b
    28 jnz a -19
    # Steps 09 - 26 is:
        r = register before step 09
        nr = register after step 27
        nr[a] = floor(r[a])
        nr[b] = r[a] % 2
        nr[c] = 0



    29 jnz 1 -21


"""





def evaluate_word(w: str, r):
    if w.isalpha():
        return r[w]
    else:
        return int(w)

instructions = input_string.splitlines()


def is_sequence_valid(s):
    for i, c in enumerate(s):
        if c != str(i % 2):
            return False
    return True


def build_state(r, i):
    return (r['a'], r['b'], r['c'], r['d'], i)


def is_success(a: int):
    r = {
        'a': a,
        'b': 0,
        'c': 0,
        'd': 0
    }
    current_instruction = 0
    current_sequence = ""
    past_states = {}

    """
    To check that it is infinitely looping correctly
    -   The sequence before looping must be valid
    -   The sequence created during the loop must be valid
    
    
    For each iteration, 
        if sequence is invalid:
            immediate fail
        if current state is a key in past_states:
            We have been here before. 
            Check if we are able to produce a correct infinite sequence
                past_state.sequence and current_state.sequence must both be valid
                and the difference added onto current_state.sequence must also be valid
        else
            Add current sate to past_states
            compute next state
    """



    iterations = 0
    while 0 <= current_instruction < len(instructions) and iterations < 5000:
        # if not is_sequence_valid(current_sequence):
        #     # print("invalid sequence", current_sequence)
        #     return False

        current_state = build_state(r, current_instruction)
        # if current_state in past_states:
        #     # check if this is a valid infinite sequence
        #     print("Maybe infinite sequence?")
        #     print("past", past_states[current_state])
        #     print("current", current_sequence)
        #     return True
        past_states[current_state] = current_sequence

        words = instructions[current_instruction].split()

        if current_instruction == 29 or current_instruction == 28:
            iterations += 1
            print(r, "\t", current_instruction, instructions[current_instruction])
            # print(current_sequence)

        if current_instruction == 2:
            r['d'] = r['d'] + 182 * r['c']
            r['b'] = 0
            r['c'] = 0
            current_instruction = 8
        elif current_instruction == 12:
            r['a'] = int(r['b'] / 2)
            r['c'] = 2 if r['b'] % 2 == 0 else 1
            r['b'] = 0
            current_instruction = 20
        elif current_instruction == 21:
            r['b'] = r['b'] - r['c']
            r['c'] = 0
            current_instruction = 26

        elif current_instruction == 28:
            if r['a'] == 0:
                current_instruction += 1
            else:
                r['b'] = r['a'] % 2
                r['a'] = int(r['a']/2)
                r['c'] = 0
                current_instruction = 26
        else:

            if words[0] == "cpy":
                if not words[2].isalpha():
                    pass
                else:
                    r[words[2]] = evaluate_word(words[1], r)
                current_instruction += 1
            elif words[0] == "inc":
                if not words[1].isalpha():
                    pass
                else:
                    r[words[1]] += 1
                current_instruction += 1
            elif words[0] == "dec":
                if not words[1].isalpha():
                    pass
                else:
                    r[words[1]] -= 1
                current_instruction += 1
            elif words[0] == "jnz":
                if evaluate_word(words[1], r) == 0:
                    current_instruction += 1
                else:
                    if not words[2].isalpha():
                        current_instruction += int(words[2])
                    else:
                        current_instruction += r[words[2]]
            elif words[0] == "out":
                current_sequence += str(evaluate_word(words[1], r))
                current_instruction += 1
            else:
                print("unknown instruction for", a)
                return False

    print("program terminated")
    print(current_sequence)
    return False

# 6 should give 01011111
# print(is_success(6))
# print(is_success(182))


# i = 0
# while True:
#     i += 1
#     print("checking", i)
#     is_success(i)
#     # if is_success(i):
#     #     print("success", i)
#     print("-----")






"""

After examining the state of the registers on instructions 28 and 29, it is pretty clear what is going on
e.g.
{'a': 1277, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 638, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 319, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 159, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 79, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 39, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 19, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 9, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 4, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 2, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 1, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 0, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 0, 'b': 1, 'c': 0, 'd': 2554} 	 29 jnz 1 -21
{'a': 1277, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 638, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 319, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 159, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 79, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 39, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 19, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 9, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 4, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 2, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 1, 'b': 0, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 0, 'b': 1, 'c': 0, 'd': 2554} 	 28 jnz a -19
{'a': 0, 'b': 1, 'c': 0, 'd': 2554} 	 29 jnz 1 -21



In short: 
- The output is entirely dictated by the b register
- The b register is determined by the oddness of the a register from the previous state
- instruction 29 always has the same state, i.e. it is infinitely looping back to 08
- the d register determines the initial value for a at the start of the infinite loop
- the d register is determined by initial value of register a + 2548 (r['a'] + 2548)
- with the understanding of how b is generated, we can work backwards to determine what number generates
    the desired output
- when  
a = 0 -> b will be a 1 because the previous value of a was a 1
- when 
a = 1 -> b will be 0 if previous value of a was a 2, or 1 if previous value of a was 3.
obviously, we want a previous value of a to be 2 to give us the b=0
a = 2 -> b will be 0 if previous value of a was a 4, or 1 if previous value of a was 5.
obviously, we want a previous value of a to be 5

we can keep repeating this, until we find the smallest even value that is greater than 2548.
    (We want even because we want the first character of the sequence to be a 0. We already
    know that the last part of the loop will output a 1)
then we can subtract 2548 to give us the initial value of a

"""

current_state = (0, 1)
while current_state[0] < 2548 or current_state[0] % 2 != 0:
    current_state = (current_state[0] * 2 + current_state[1], (current_state[1] + 1)%2)
print(current_state[0] - 2548)











