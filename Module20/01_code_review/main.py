def func(students):
    list_all = []
    list_interests = [value['interests'] for key, value in students.items()]    # Формируем три списка  с интересами
    [list_all.extend(i) for i in list_interests]                                # Преобразуем три списка с интересами в один
    long = [value['surname'] for key, value in students.items()]                # формируем список из фамилий
    return list_all, long

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}



'''
Исходный код:

def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)
'''


# TODO исправить код
print('------------------------------------------------')

print('Список пар "ID студента — возраст":', [(key, value['age']) for key, value in students.items()])

print('Полный список интересов:            ', set(func(students)[0]))

print('Общая длина всех фамилий студентов: ', sum([len(i) for i in func(students)[1]]))

#  ****** Никита - посмотрите плз - не перемудрил ли я с функцией? Может - можно было ее как-то сократить в объеме кода?