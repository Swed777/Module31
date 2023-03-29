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

'''
Задача 4. Магия
Что нужно сделать
Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый. 
У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

Таблица преобразований:
Вода + Воздух = Шторм;
Вода + Огонь = Пар;
Вода + Земля = Грязь;
Воздух + Огонь = Молния;
Воздух + Земля = Пыль;
Огонь + Земля = Лава.
Напишите программу, которая реализует все эти элементы.
Каждый элемент необходимо организовать как отдельный класс. Если результат не определён, то возвращается None.

Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:

class ExampleOne:
    def __add__(self, other):
        return ExampleTwo()

class ExampleTwo:
    answer = 'сложили два класса и вывели'

first_example = ExampleOne()
second_example = ExampleTwo()
result = first_example + second_example
print(result.answer)
Дополнительно: придумайте свой элемент (или элементы) и реализуйте его взаимодействие с остальными.'''