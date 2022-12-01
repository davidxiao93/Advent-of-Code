import file_loader

input_string = file_loader.get_input()

words = input_string.split()
highest_marble = int(words[-2]) * 100 # Part 2
num_players = int(words[0])

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next if next is not None else self
        self.prev = prev if prev is not None else self


class Marbles:
    def __init__(self):
        self.current_node = Node(0)

    def insert(self, marble):
        score = 0
        if marble % 23 == 0:
            marble_to_remove = self.current_node.prev.prev.prev.prev.prev.prev.prev
            left_node = marble_to_remove.prev
            right_node = marble_to_remove.next
            left_node.next = right_node
            right_node.prev = left_node
            self.current_node = right_node
            score = marble_to_remove.data + marble
        else:
            left_node = self.current_node.next
            right_node = self.current_node.next.next
            new_node = Node(marble, right_node, left_node)
            left_node.next = new_node
            right_node.prev = new_node
            self.current_node = new_node
        return score

    def pretty_print(self):
        ms = [self.current_node.data]
        next_node = self.current_node.next
        while next_node.data not in ms:
            ms.append(next_node.data)
            next_node = next_node.next
        print(" ".join([str(m) for m in ms]))


marbles = Marbles()
elf_scores = {}
for marble in range(1, highest_marble + 1):
    score = marbles.insert(marble)
    if score != 0:
        elf = ((marble - 1) % num_players) + 1
        if elf not in elf_scores:
            elf_scores[elf] = 0
        elf_scores[elf] += score

print(max(elf_scores.values()))


