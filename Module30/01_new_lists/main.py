# TODO здесь писать код
from functools import reduce
from typing import List


def my_multiply(a: int, b: int) -> int:
    result = a * b
    # print(f"{a} * {b} = {result}")        # Оставил на память - ЕИ
    return result


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# _________________________________________________

my_floats: List[float] = list(map(lambda x: round(x ** 3, 3), floats))
my_names: List[str] = list(filter(lambda letter: len(letter) >= 5, names))

print('Задание 1:', my_floats)
print('Задание 2:', my_names)
print('Задание 3:', reduce(my_multiply, numbers))

# зачтено
