# TODO здесь писать код
def control(file):
    pref = '@№$%^&*()'
    ext = ('.txt', '.docx')
    for i in pref:
        if file.startswith(i) == True:
            print("Ошибка: название начинается на один из специальных символов --> {}".format(i))
            return
    if not file.endswith(ext):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
    else:
        print("Файл назван верно")

name = input('Название файла: ')
control(name)