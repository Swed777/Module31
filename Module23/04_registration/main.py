# TODO здесь писать код

def validata(i_line, count_string):
    result = True
    try:
        client = i_line.split()  # разбиваем строку по признаку "Пробел"
        name, post, age = client[0], client[1], client[2]  # Множественное присваивание элементам строки
    except (IndexError):
        result = False
        bad_logfile.write(f'\nВ строке нр {count_string}: --> {i_line.strip()} <-- отсутствует одновременно ТРИ поля')
    return result

count_string = 0 # счетчик всех строк в файле

# Открываем исходный файл и два файла с логами
with open('registrations.txt', 'r', encoding='utf8') as open_file:
    fin = open_file.readlines()
good_logfile = open('registrations_good.log','a', encoding='utf8')
bad_logfile  = open('registrations_bad.log', 'a', encoding='utf8')


for i_line in fin:
    count_string += 1
    if validata(i_line, count_string):
        good_logfile.write(f'{i_line}')
    else:
        pass

# Закрываем все файлы
open_file.close()
good_logfile.close()
bad_logfile.close()







'''
Задача 3. Регистрация
Что нужно сделать
У вас есть файл с протоколом регистрации пользователей на сайте — registrations.txt. Каждая строка содержит имя, имейл и возраст, разделённые пробелами. Например: Василий test@test.ru 27.

Напишите программу, которая проверяет данные из файла для каждой строки:

Присутствуют все три поля.
Поле «Имя» содержит только буквы.
Поле «Имейл» содержит @ и точку.
Поле «Возраст» представляет число от 10 до 99.
В результате проверки сформируйте два файла:

registrations_good.log для правильных данных; записывать строки как есть;
registrations_bad.log — для ошибочных; записывать строку и вид ошибки.
Для валидации строки данных напишите функцию, которая может выдавать исключения:

НЕ присутствуют все три поля: IndexError.
Поле «Имя» содержит НЕ только буквы: NameError.
Поле «Имейл» НЕ содержит @ и точку: SyntaxError.
Поле «Возраст» НЕ представляет число от 10 до 99: ValueError.
Формат выходных данных

Содержимое файла registrations_bad.log:

Ольга kmrn@gmail.com 123        Поле «Возраст» НЕ представляет число от 10 до 99

Чехова kb@gmail.com 142        Поле «Возраст» НЕ представляет число от 10 до 99

……

Степан ky 59        Поле «Имейл» НЕ содержит @ и точку

……

Содержимое файла registrations_good.log:

Геннадий ttdababmt@gmail.com 69

Ольга ysbxur@gmail.com 20

……

Советы и рекомендации
Помните, что пайтон не всегда будет выполнять операции, которые вы предполагали, например:
if '1' and '2' in строка — по приоритету операций сперва будет выполнено действие с in, а уже потом and. Значит, пайтон не будет в этом случае искать 1 внутри строки. 
Элементы а, б, с: разделять объект (например, список) на несколько переменных очень удобно при помощи множественного присваивания. Но если элементов в списке окажется меньше, чем указанных переменных, то появится ошибка.
При необходимости вы можете объединять исключения в except-блоке. Для этого нужно перечислить классы исключений, которые вы хотите отследить в кортеже: 
except (DrunkError, CarCrashError...) as exc
    As exc в данном случае сработает так же, как и с файлами в конструкции with open(...) as file. То есть пайтон запишет пойманное исключение в переменную с названием exc (название может быть любым).
При переезде зачастую нужно вынести много коробок с вещами из дома. Если для переноса каждой коробки придётся открывать/закрывать двери, то на это уйдет много сил. Их уйдет меньше, если получится открыть двери один раз и закрыть, когда всё будет сделано. То же самое справедливо и для файлов. Старайтесь открывать и закрывать их экономно, например, открыть файлы можно до цикла, а закрыть — после (если нет необходимости переоткрывать файл внутри цикла).
'''