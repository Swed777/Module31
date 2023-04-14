# TODO здесь писать код
class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm.name
        elif isinstance(other, Fire):
            return Steam.name
        elif isinstance(other, Earth):
            return Dirt.name


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lighting.name
        elif isinstance(other, Earth):
            return Dust.name


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava.name


class Earth:
    name = 'Земля'


class Storm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Dirt:
    name = 'Грязь'


class Lighting:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'
    # def __str__(self):
    # return "Тест на память"


print(Water() + Air())
print(Water() + Fire())
print(Water() + Earth())
print(Air() + Fire())
print(Air() + Earth())
print(Fire() + Earth())

# print(Earth() + Fire()) -  для сложения при перестановке слагаемых нужно прописать в классах также обратные действия. Если нужно - пропишу


# print(Lava()) # для задания лишнее, оставил на память для изучения метода __str__(self)

# зачтено
