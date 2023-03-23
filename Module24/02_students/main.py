class Student:
    fio = ''
    num_of_group = ''
    grade = tuple()
def list_group():
        Student.fio = input('Введите имя и фамилию: ')
        Student.num_of_group = input('Введите номер группы: ')
        Student.grade = tuple(input('Введите 5 оценок через пробел: ').split())
        Student.grade.median = sum([int(i) for i in Student.grade])/5 # преобразование в int
        return Student.fio, Student.num_of_group, Student.grade, Student.grade.median

# def custom_key(list_grade):
#     return (sum(list_student[2]))

list_student = []
summ = 0
for _ in range(2):
    list_student.append(list_group())
    # list_student.sort(key=lambda x: x.give_average())
    print(Student.grade)
print(list_student)
# list_student.sort(key=(sum(Student.grade)) / 5)
print('Список студентов отсортированный:')
list_student.sort()
print(list_student)



'''
Задача 2. Студенты
Что нужно сделать
Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя) 
 и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

'''