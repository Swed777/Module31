# TODO здесь писать код
class Student:
    def __init__(self, fio, num_of_group, grade):
        self.fio = fio
        self.num_of_group = num_of_group
        self.grade = grade

    def __str__(self):
        return ('Список групп:', self.fio, self.num_of_group, self.grade)
def list_group():
    name = input('Введите имя и фамилию: ')
    fi   = input('Введите номер группы: ')
    ball = tuple(input('Введите 5 оценок через пробел: ').split())
    return (name, fi, ball)


list_student = []
for _ in range(2):
    x = Student(*list_group())
    list_student.append(x)
print('Список студентов: ')
print(list_student)
for i_stud in list_student:
     print(i_stud)


'''
Задача 2. Студенты
Что нужно сделать
Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя) 
 и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

'''