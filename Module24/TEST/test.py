class Student:
        fio = ''
        num_of_group = ''
        grade = tuple()
def list_group():
            Student.fio = input('Введите имя и фамилию: ')
            Student.num_of_group   = input('Введите номер группы: ')
            Student.grade = tuple(input('Введите 5 оценок через пробел: ').split())
            return Student.fio, Student.num_of_group, Student.grade
# def give_average():
#         return round(sum(Student.grade) / len(Student.grade))

list_student = []
summ = 0
for _ in range(2):
     list_student.append(list_group())
     # list_student.sort(key=lambda x: x.give_average())
     print(Student.grade)
     for i in Student.grade:    # находим сумму баллов для каждого студента
        summ += int(i)
     print(summ)
print(list_student)



