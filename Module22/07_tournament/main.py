# TODO здесь писать код

with open('first_tour.txt', 'r') as open_file:
    text = open_file.readlines()  # Открываем файл построчно
    min_level = text[0]  # определяем минимальный проходной балл
    count_us = (i_level for i_level in text[1::] if i_level.split()[
        2] > min_level)  # формируем список из проходящих во второй тур по минимальному баллу (см.цикл ниже)
    lider_list = list(count_us)

with open('second_tour.txt', 'a') as open_file:
    open_file.write(str(len(lider_list)))  # Запиываем в 1 строку количество участников второго этапа
    open_file.close()

spisok_sort = []
for i, num in enumerate(
        lider_list):  # формируем список списков участников второго этапа и сортируем его по убываню очков
    spisok_sort.append(lider_list[i].split())
    spisok_sort.sort(key=lambda x: x[2], reverse=True)  # Сортировать по третьему элементу (баллам)

for i, num in enumerate(spisok_sort):
    out_text = (f'\n{i + 1}) {num[1][0]}. {num[0]} {num[2]} ')
    with open('second_tour.txt', 'a') as open_file:
        open_file.write(out_text)

# зачтено
