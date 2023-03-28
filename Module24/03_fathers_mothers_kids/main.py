# TODO здесь писать код
from random import randint
class Parent:
    'Класс для описания родителей'
    def __init__(self, name, age, lst_chld):
        self.name = name
        self.age = age
        self.list_of_chld = lst_chld
    #
    # def add_cldrn(self, children):
    #     self.list_of_chld.append(children)

    def print_info(self):
        print(' Имя: {}\n Возраст: {}\n Список детей: {}\n'.format(self.name, self.age, self.list_of_chld))

class Children:
    'Класс для описания детей'
    def __init__(self, name, age, status_relax, status_hunger):
        self.name = name
        self.age = age
        self.status_relax = status_relax
        self.status_hunger = status_hunger

    def print_info(self):
        print(' Имя: {}\n Возраст: {}\n Спокоен?: {}\n Голоден?: {}\n'.format(self.name, self.age, self.status_relax, self.status_hunger))

    def get_status(self):
        return (self.name, self.age, self.status_relax, self.status_hunger)

def parnt():
    Parent.name = input('Имя родителя: ')
    Parent.age = int(input('Возраст родителя: '))
    Parent.list_of_chld = ()

son = Children('Andry', 5, randint(0,1), randint(0,1))
dother = Children('Mary', 7, randint(0,1), randint(0,1))
# son.print_info()

# Father = Parent('Anatoliy Ivanovich', 35, [son.__dict__, dother.__dict__])
Father = Parent('Anatoliy Ivanovich', 35, [son.get_status(), dother.get_status()])
Father.print_info()
son.print_info()
dother.print_info()



'''
Задача 3. Отцы, матери и дети
Что нужно сделать
Реализуйте два класса: «Родитель» и «Ребёнок». 

У родителя есть:
имя,
возраст,
список детей.

И он может:
сообщить информацию о себе,
успокоить ребёнка,
покормить ребёнка.

У ребёнка есть:
имя,
возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
состояние спокойствия,
состояние голода.

Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, 
и что-то поинтереснее.
'''