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
