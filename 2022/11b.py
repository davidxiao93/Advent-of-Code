from typing import Callable, Dict, List

import file_loader

input_string = file_loader.get_input()

class Monkey:
    def __init__(self, id: int, operation: Callable[[int], int], test: int, test_true: int, test_false: int):
        self.id = id
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false

monkey_ids: List[int] = []
monkeys: Dict[int, Monkey] = dict()
monkey_holdings: Dict[int, List[int]] = dict()
monkey_inspections: Dict[int, int] = dict()

def square(old):
    return old * old

def add(amount):
    def add_amount(old):
        return old + amount
    return add_amount

def multiply(amount):
    def multiply_amount(old):
        return old * amount
    return multiply_amount

global_modulus = 1

for monkey_lines in input_string.split("\n\n"):
    lines = monkey_lines.splitlines()
    monkey_id = int(lines[0].split()[-1][:-1])
    items = [int(x.strip()) for x in lines[1].split(":")[1].split(",")]
    operator = lines[2].split()[-2]
    operand = lines[2].split()[-1]
    if operand == "old":
        operation = square
    elif operator == "*":
        operation = multiply(int(operand))
    elif operator == "+":
        operation = add(int(operand))
    else:
        raise Exception
    test = int(lines[3].split()[-1])
    global_modulus = global_modulus * test
    test_true = int(lines[4].split()[-1])
    test_false = int(lines[5].split()[-1])

    monkey = Monkey(monkey_id, operation, test, test_true, test_false)
    monkey_ids.append(monkey_id)
    monkeys[monkey_id] = monkey
    monkey_holdings[monkey_id] = items
    monkey_inspections[monkey_id] = 0

monkey_index = 0
for i in range(10_000):
    for id in monkey_ids:
        monkey = monkeys[id]
        for item in monkey_holdings[id]:
            monkey_inspections[id] += 1
            new_value = monkey.operation(item) % global_modulus
            if new_value % monkey.test == 0:
                monkey_holdings[monkey.test_true].append(new_value)
            else:
                monkey_holdings[monkey.test_false].append(new_value)
        monkey_holdings[id] = []

v = sorted(monkey_inspections.values())

print(v[-1] * v[-2])