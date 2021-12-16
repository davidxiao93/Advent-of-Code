from typing import Tuple, List

input = """420D598021E0084A07C98EC91DCAE0B880287912A925799429825980593D7DCD400820329480BF21003CC0086028910097520230C80813401D8CC00F601881805705003CC00E200E98400F50031801D160048E5AFEFD5E5C02B93F2F4C11CADBBB799CB294C5FDB8E12C40139B7C98AFA8B2600DCBAF4D3A4C27CB54EA6F5390B1004B93E2F40097CA2ECF70C1001F296EF9A647F5BFC48C012C0090E675DF644A675DF645A7E6FE600BE004872B1B4AAB5273ED601D2CD240145F802F2CFD31EFBD4D64DD802738333992F9FFE69CAF088C010E0040A5CC65CD25774830A80372F9D78FA4F56CB6CDDC148034E9B8D2F189FD002AF3918AECD23100953600900021D1863142400043214C668CB31F073005A6E467600BCB1F4B1D2805930092F99C69C6292409CE6C4A4F530F100365E8CC600ACCDB75F8A50025F2361C9D248EF25B662014870035600042A1DC77890200D41086B0FE4E918D82CC015C00DCC0010F8FF112358002150DE194529E9F7B9EE064C015B005C401B8470F60C080371460CC469BA7091802F39BE6252858720AC2098B596D40208A53CBF3594092FF7B41B3004A5DB25C864A37EF82C401C9BCFE94B7EBE2D961892E0C1006A32C4160094CDF53E1E4CDF53E1D8005FD3B8B7642D3B4EB9C4D819194C0159F1ED00526B38ACF6D73915F3005EC0179C359E129EFDEFEEF1950005988E001C9C799ABCE39588BB2DA86EB9ACA22840191C8DFBE1DC005EE55167EFF89510010B322925A7F85A40194680252885238D7374C457A6830C012965AE00D4C40188B306E3580021319239C2298C4ED288A1802B1AF001A298FD53E63F54B7004A68B25A94BEBAAA00276980330CE0942620042E3944289A600DC388351BDC00C9DCDCFC8050E00043E2AC788EE200EC2088919C0010A82F0922710040F289B28E524632AE0"""

binary_input = bin(int(input, 16))[2:].zfill(len(input) * 4)

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



