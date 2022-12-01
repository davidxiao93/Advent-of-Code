from typing import Tuple, List

import file_loader

input_string = file_loader.get_input()

binary_input = bin(int(input_string, 16))[2:].zfill(len(input_string) * 4)

class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type

    def evaluate(self) -> int:
        raise NotImplementedError()

class LiteralPacket(Packet):
    def __init__(self, version, type, value):
        super().__init__(version, type)
        self.value = value

    def evaluate(self):
        return self.value

class OperatorPacket(Packet):
    def __init__(self, version, type, packets: List[Packet]):
        super().__init__(version, type)
        self.packets = packets

    def evaluate(self) -> int:
        packet_values = [p.evaluate() for p in self.packets]
        if self.type == 0:
            # sum
            return sum(packet_values)
        elif self.type == 1:
            # product
            result = 1
            for v in packet_values:
                result *= v
            return result
        elif self.type == 2:
            # min
            return min(packet_values)
        elif self.type == 3:
            # max
            return max(packet_values)
        elif self.type == 5:
            # greater than
            return 1 if packet_values[0] > packet_values[1] else 0
        elif self.type == 6:
            # less than
            return 1 if packet_values[0] < packet_values[1] else 0
        elif self.type == 7:
            # equality
            return 1 if packet_values[0] == packet_values[1] else 0
        else:
            raise NotImplementedError

def parse_packet(remaining_input: str) -> Tuple[str, Packet]:
    version = int(remaining_input[:3], 2)
    type = int(remaining_input[3:6], 2)
    remaining_input = remaining_input[6:]

    if type == 4:
        # literal packet
        packet_contents = ""
        while True:
            is_last = remaining_input[0] == "0"
            packet_contents += remaining_input[1:5]
            remaining_input = remaining_input[5:]
            if is_last:
                break
        packet_value = int(packet_contents, 2)
        return remaining_input, LiteralPacket(version, type, packet_value)
    else:
        # operator packet
        length_type_id = int(remaining_input[0], 2)
        remaining_input = remaining_input[1:]
        if length_type_id == 0:
            num_bits_to_use = int(remaining_input[:15], 2)
            remaining_input = remaining_input[15:]
            original_length = len(remaining_input)
            sub_packets = []
            while len(remaining_input) > original_length - num_bits_to_use:
                remaining_input, packet = parse_packet(remaining_input)
                sub_packets.append(packet)
            return remaining_input, OperatorPacket(version, type, sub_packets)
        else:
            num_packets_to_find = int(remaining_input[:11], 2)
            remaining_input = remaining_input[11:]
            sub_packets = []
            while len(sub_packets) < num_packets_to_find:
                remaining_input, packet = parse_packet(remaining_input)
                sub_packets.append(packet)
            return remaining_input, OperatorPacket(version, type, sub_packets)


_, p = parse_packet(binary_input)

print(p.evaluate())



