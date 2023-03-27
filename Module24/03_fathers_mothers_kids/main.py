# TODO здесь писать код
class Parent:
    'Класс для описания родителей'
    # name = ''
    # age = 0
    # list_of_chld = []
    def __init__(self, name, age, lst_chld):
        self.name = name
        self.age = age
        self.list_of_chld = lst_chld

    def add_cldrn(self, children):
        self.list_of_chld.append(children)

    def print_info(self):
        print('Имя: {}\n Возраст: {}\n Список детей: {}\n'.format(self.name, self.age, self.list_of_chld))

class Children:
    'Класс для описания детей'
    name = ''
    age = 0
    status_relax = True
    status_hunger = True


def parnt():
    Parent.name = input('Имя родителя: ')
    Parent.age = int(input('Возраст родителя: '))
    Parent.list_of_chld = ()
#
# parent1 = Parent()
# parent1.print_info()
#
# parent1.add_cldrn('Mary')
# parent1.add_cldrn('Jonny')
# parent1.print_info()

# spisok = ['nadya', 'vera']
Father = Parent('Kolya', 35, ['nadya', 'vera'])
Father.print_info()

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