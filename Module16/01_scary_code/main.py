# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
a.count(5)
print('Кол-во цифр 5 при первом объединении: ', a.count(5))
for i in a:         #
    if i == 5:
        a.remove(i)

a.extend(c)
print('Кол-во цифр 3 при втором объединении: ', a.count(3))
print('Итоговый список: ', a)

