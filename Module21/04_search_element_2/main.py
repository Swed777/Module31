# TODO здесь писать код

def search_key(data, key, depth=None, level=1):
    result = None

    if depth and depth < level:
        return None
    if key in data:
        return data[key]
    for i_teg in data.values():
        if isinstance(i_teg, dict):
            result = search_key(i_teg, key, depth, level=level + 1)
            if result:
                break
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
level = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if level == 'y':
    depth = int(input('Введите максимальную глубину: '))
elif level == 'n':
    depth = None

print('Значение ключа: ', search_key(data=site, depth=depth, key=key))

# зачтено
