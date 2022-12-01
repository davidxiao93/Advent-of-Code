import file_loader

input_string = file_loader.get_input()

# input_string = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2"""



def evaluate(r, w: str):
    if w.isalpha():
        if w not in r:
            r[w] = 0
        return r[w]
    return int(w)

class Program:
    def __init__(self, instructions, registers):
        self.instructions = instructions
        self.registers = registers
        self.current_instruction = 0
        self.in_queue = []
        self.out_queue = []
        self.is_blocked = False
        self.is_terminated = False

    def execute(self):
        if self.current_instruction < 0 or len(self.instructions) <= self.current_instruction:
            self.is_terminated = True
            return
        instruction = self.instructions[self.current_instruction]
        words = instruction.split()
        if words[0] == "snd":
            self.out_queue.append(evaluate(self.registers, words[1]))
            self.current_instruction += 1
        elif words[0] == "set":
            self.registers[words[1]] = evaluate(self.registers, words[2])
            self.current_instruction += 1
        elif words[0] == "add":
            if words[1] not in self.registers:
                self.registers[words[1]] = 0
            self.registers[words[1]] += evaluate(self.registers, words[2])
            self.current_instruction += 1
        elif words[0] == "mul":
            if words[1] not in self.registers:
                self.registers[words[1]] = 0
            self.registers[words[1]] *= evaluate(self.registers, words[2])
            self.current_instruction += 1
        elif words[0] == "mod":
            if words[1] not in self.registers:
                self.registers[words[1]] = 0
            self.registers[words[1]] = self.registers[words[1]] % evaluate(self.registers, words[2])
            self.current_instruction += 1
        elif words[0] == "rcv":
            if len(self.in_queue) != 0:
                self.registers[words[1]] = self.in_queue.pop(0)
                self.current_instruction += 1
                self.is_blocked = False
            else:
                self.is_blocked = True
        elif words[0] == "jgz":
            if evaluate(self.registers, words[1]) > 0:
                self.current_instruction += evaluate(self.registers, words[2])
            else:
                self.current_instruction += 1



p0 = Program(instructions=input_string.splitlines(), registers={'p': 0})
p1 = Program(instructions=input_string.splitlines(), registers={'p': 1})

p1_sent = 0

while True:
    while len(p0.out_queue) != 0:
        p1.in_queue.append(p0.out_queue.pop(0))
    while len(p1.out_queue) != 0:
        p1_sent += 1
        p0.in_queue.append(p1.out_queue.pop(0))
    p0.execute()
    p1.execute()
    if p0.is_terminated and p1.is_terminated:
        # print("both programs terminated")
        break
    if p0.is_blocked and p1.is_blocked:
        # print("both programs blocked")
        break

# print("end")
print(p1_sent)




