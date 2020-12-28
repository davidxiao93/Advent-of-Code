import hashlib
from typing import Set, Optional

input = """zpqevtbw"""

# input = """abc"""



cache_md5 = {}
def md5(n: int) -> str:
    if n not in cache_md5:
        cache_md5[n] = hashlib.md5((input + str(n)).encode('utf-8')).hexdigest()
    return cache_md5[n]


def get_triples(n: int) -> Optional[str]:
    h = md5(n)
    for a, b, c in zip(h, h[1:], h[2:]):
        if a == b == c:
            return a
    return None

def contains_5_in_row(n: int, c: str) -> bool:
    h = md5(n)
    return c*5 in h

current_index = 0
set_found_hashes = set()

while len(set_found_hashes) < 64:
    triples = get_triples(current_index)
    if triples is not None:
        for i in range(1, 1001):
            if contains_5_in_row(current_index + i, triples):
                set_found_hashes.add(current_index)
                if len(set_found_hashes) == 64:
                    print(current_index)
    current_index += 1
