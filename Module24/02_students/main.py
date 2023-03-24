class Student:
    fio = ''
    num_of_group = ''
    grade = tuple()
def list_group():
        Student.fio = input('Введите имя и фамилию: ')
        Student.num_of_group = int(input('Введите номер группы: '))
        Student.grade = tuple(input('Введите 5 оценок через пробел: ').split())
        Student.grade_median = sum([int(i) for i in Student.grade])/5 # преобразование в int
        return Student.fio, Student.num_of_group, Student.grade, Student.grade_median

list_student = []
summ = 0
for _ in range(2):
    list_student.append(list_group())
print('Список студентов первоначальный: ')
print(list_student)
print('Список студентов отсортированный:')
print(list_student.sort(key=lambda x: x[3]))




'''
Задача 2. Студенты
Что нужно сделать
Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя) 
 и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

'''