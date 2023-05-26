# TODO здесь писать код
from collections import Counter


def can_be_poly(letters: str) -> bool:
    return sum(x % 2 for x in Counter(letters).values()) <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

# зачтено
