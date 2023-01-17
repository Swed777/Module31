# TODO здесь писать код

def new_contact():
    fio = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if fio in contact:
        print('Такой человек уже есть в контактах \n')
    else:
        phone = input('Введите номер телефона: ')
        contact[fio] = phone
    print('Текущий словарь контактов: ', contact)


def search_contact():
    search = input('Введите фамилию для поиска: ')
    for i, number in contact.items():
        if search == i[1]:
            print(i[0], i[1], number)


contact = {}

while True:
    menu = int(
        input('Введите номер действия: \n 1. Добавить контакт  \n 2. Найти человека \n----------------------  \n'))
    if menu == 1:
        new_contact()
    if menu == 2:
        search_contact()

# зачтено
