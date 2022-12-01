from typing import Dict

import file_loader

input_string = file_loader.get_input()


"""
 0000
1    2
1    2
 3333
4    5
4    5
 6666
"""

segments = {
    0: {0, 1, 2, 4, 5, 6},
    1: {2, 5},
    2: {0, 2, 3, 4, 6},
    3: {0, 2, 3, 5, 6},
    4: {1, 2, 3, 5},
    5: {0, 1, 3, 5, 6},
    6: {0, 1, 3, 4, 5, 6},
    7: {0, 2, 5},
    8: {0, 1, 2, 3, 4, 5, 6},
    9: {0, 1, 2, 3, 5, 6}
}

def decode_signals(signals) -> Dict[str, int]:
    seven_segments = set([s for s in signals if len(s) == 3][0])
    one_segments = set([s for s in signals if len(s) == 2][0])
    four_segments = set([s for s in signals if len(s) == 4][0])

    segment_0 = seven_segments - one_segments
    segment_25 = one_segments
    segment_13 = four_segments - one_segments
    segment_46 = (set("abcdefg") - seven_segments) - four_segments

    three_segments = set([s for s in signals if len(s) == 5 and segment_25.issubset(set(s))][0])
    segment_036 = three_segments - segment_25
    segment_36 = segment_036 - segment_0
    segment_3 = segment_36 - segment_46
    segment_6 = segment_36 - segment_13
    segment_1 = segment_13 - segment_3
    segment_4 = segment_46 - segment_6

    six_segments = set([s for s in signals if len(s) == 6 and not segment_25.issubset(set(s))][0])
    segment_2 = segment_25 - six_segments
    segment_5 = segment_25 - segment_2

    return {
        segment_0.pop(): 0,
        segment_1.pop(): 1,
        segment_2.pop(): 2,
        segment_3.pop(): 3,
        segment_4.pop(): 4,
        segment_5.pop(): 5,
        segment_6.pop(): 6,
    }













def decode_output(value, segment_mapping: Dict[str, int]) -> int:
    on_segments = set()
    for v in value:
        on_segments.add(segment_mapping[v])

    for v, s in segments.items():
        if on_segments == s:
            return v
    raise Exception("unknown segment")

def decode_line(line) -> int:
    signals = line.split("|")[0].strip().split(" ")
    outputs = line.split("|")[1].strip().split(" ")

    segment_mapping = decode_signals(signals)
    return 1000 * decode_output(outputs[0], segment_mapping) \
         +  100 * decode_output(outputs[1], segment_mapping) \
         +   10 * decode_output(outputs[2], segment_mapping) \
         +        decode_output(outputs[3], segment_mapping)




print(sum([
    decode_line(line)
    for line in input_string.splitlines()
]))
