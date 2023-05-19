# TODO здесь писать код
import math
from abc import ABC

class MyMath(ABC):
    """
    Абстрактный класс MyMath
    """
    @classmethod
    def circle_len(cls, radius: int) -> float:          # вычисление длины окружности,
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:               # вычисление площади круга,
        return math.pi * radius ** 2

    @classmethod
    def cube_value(cls, rib: int) -> float:                    # вычисление объёма куба,
        return rib ** 3

    @classmethod
    def sphere_area(cls, radius: int) -> float:                    # вычисление площади поверхности сферы.
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_value(rib=7)
res_4 = MyMath.sphere_area(radius=8)

print(round(res_1, 2))
print(round(res_2, 2))
print(round(res_3, 2))
print(round(res_4, 2))

'''
Задача 2. Математический модуль
Что нужно сделать
Вася использует в своей программе очень много различных математических вычислений, связанных с фигурами.
 Например, нахождение их площадей или периметров. Поэтому, чтобы не захламлять код огромным количеством функций,
он решил выделить для них отдельный класс, подключить как модуль и использовать по аналогии с модулем math.

Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):

вычисление длины окружности,
вычисление площади окружности,
вычисление объёма куба,
вычисление площади поверхности сферы.
Пример основного кода:

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

Результат:
31.41592653589793
113.09733552923255
'''