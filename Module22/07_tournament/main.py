# TODO здесь писать код

count_user = 0
with open('first_tour.txt', 'r') as open_file:
    text = open_file.readlines()
    min_level = text[0]
    count_us = (int(i_level.split()[2]) for i_level in text[1::] if i_level.split()[2] > min_level)  # см внизу обычный цикл
    # count_us = (int(i_level.split()[2]) for i_level in text[1::] if i_level.split()[2] > min_level)  # см внизу обычный цикл
    numbers = len(list(count_us))
    print(numbers)
    with open('second_tour.txt', 'w') as open_file:
        open_file.write(str(numbers))


    # print(text[0])





    # ЗАготовка для генератора
    # for i_level in text[1::]:
    #     if i_level.split()[2] > min_level:
    #         count_user += 1
    # print(count_user)





'''
Задача 7. Турнир
Что нужно сделать
В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в первом туре. Во второй тур проходят участники, которые набрали более K баллов в первом туре. 
Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур, с нумерацией. 
В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.

Пример:
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Segeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78

Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92'''