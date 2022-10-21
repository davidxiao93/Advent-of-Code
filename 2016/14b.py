import hashlib
from typing import Set, Optional

input = """zpqevtbw"""

# input = """abc"""

md5_cache = {}
def md5(s: str) -> str:
    if s not in md5_cache:
        md5_cache[s] = hashlib.md5(s.encode('utf-8')).hexdigest()
    return md5_cache[s]

hash_cache = {}
def hash(n: int) -> str:
    if n not in hash_cache:
        h = md5(input + str(n))
        for i in range(2016):
            h = md5(h)
        hash_cache[n] = h
    return hash_cache[n]

def get_triples(n: int) -> Optional[str]:
    h = hash(n)
    for a, b, c in zip(h, h[1:], h[2:]):
        if a == b == c:
            return a
    return None

def contains_5_in_row(n: int, c: str) -> bool:
    h = hash(n)
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
