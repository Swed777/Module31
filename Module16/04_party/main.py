guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: ')
    question = input('Гость пришёл или ушёл? ')
    if question == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name)
            print(f'Привет, {name}!')
        else:
            print(f'Извини, {name}, но мест нет')
    elif question == 'ушел':
            name = input('Имя гостя: ')
            guests.remove(name)
            print(f'Пока, {name}!')
    elif question == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.' )
        break


