# TODO здесь писать код

etalon_vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
text = input('Введите текст: ')
vowels = [i_letter for i_letter in text if i_letter in etalon_vowels]

print('Список гласных букв: ', vowels)
print('Длина списка:        ', len(vowels))