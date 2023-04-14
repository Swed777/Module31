class Student:
    fio = ''
    num_of_group = ''
    grade = tuple()


def list_group():
    Student.fio = input('Введите имя и фамилию: ')
    Student.num_of_group = int(input('Введите номер группы: '))
    Student.grade = tuple(input('Введите 5 оценок через пробел: ').split())
    Student.grade_median = sum([int(i) for i in Student.grade]) / 5  # преобразование в int и среднее значение
    return Student.fio, Student.num_of_group, Student.grade, Student.grade_median


list_student = []
summ = 0
for _ in range(10):  # ФОрмируем список  помощью объектов класса
    list_student.append(list_group())

print('Список студентов отсортированный:')
print('|Ф.И.О.| Гр |        Оценки      |')
list_student.sort(key=lambda x: x[3])  # Сортируем список по среднему значению
for x in list_student:
    print(*x[:3])  # Выводим список на экран Без среднего значения

# зачтено
