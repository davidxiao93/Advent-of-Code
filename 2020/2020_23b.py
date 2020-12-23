from typing import List
input = """137826495"""

cups = [int(x) for x in input]

class Cup:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next if next is not None else self
        self.prev = prev if prev is not None else self

class Cups:
    def __init__(self, initial_sequence, target_size):
        self.min_cup = min(initial_sequence)
        self.max_cup = target_size
        start_node = Cup(initial_sequence[0])
        self.current_node = start_node
        self.data_to_node = {
            initial_sequence[0]: start_node
        }

        for v in initial_sequence[1:]:
            self.append(v)
        for i in range(len(initial_sequence) + 1, target_size + 1):
            self.append(i)

    def append(self, v):
        new_cup = Cup(v, self.current_node, self.current_node.prev)
        self.current_node.prev.next = new_cup
        self.current_node.prev = new_cup
        self.data_to_node[v] = new_cup

    def do_round(self):
        picked_up_head = self.current_node.next
        self.current_node.next = self.current_node.next.next.next.next
        picked_up_values = [picked_up_head.data, picked_up_head.next.data, picked_up_head.next.next.data]
        # print("picked up", picked_up_values)
        # pick destination value
        destination_value = self.current_node.data - 1
        if destination_value < self.min_cup:
            destination_value = self.max_cup
        while destination_value in picked_up_values:
            destination_value -= 1
            if destination_value < self.min_cup:
                destination_value = self.max_cup
        # find destination cup
        destination_cup = self.data_to_node[destination_value]
        # while destination_cup.data != destination_value:
        #     destination_cup = destination_cup.next
        # print("destination", destination_cup.data)
        # place cups back
        picked_up_head.next.next.next = destination_cup.next
        destination_cup.next = picked_up_head
        # pick new current
        self.current_node = self.current_node.next

    def pretty_print(self):
        i = self.current_node
        row = []
        while i.data not in row:
            row.append(i.data)
            i = i.next
        print(",".join([str(x) for x in row]))
#
# def do_round(cups: List[int]) -> List[int]:
#     # current cup is always at the front
#     current_cup = cups[0]
#     moved_cups = cups[1:4]
#     found = 0
#     find_value = current_cup - 1
#     if find_value < min(cups):
#         find_value = max(cups)
#     while not found:
#         new_index = cups.index(find_value)
#         if new_index >= 4:
#             found = new_index
#         else:
#             find_value -= 1
#             if find_value < min(cups):
#                 find_value = max(cups)
#     return cups[4: found+1] + moved_cups + cups[found + 1:] + [cups[0]]

cs = Cups(cups, 1000000)

for i in range(10000000):
    cs.do_round()
print(cs.data_to_node[1].next.data * cs.data_to_node[1].next.next.data)
