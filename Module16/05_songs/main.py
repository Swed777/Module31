violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
#-----------------------------------
time_all = 0

quantity = int(input('Сколько песен выбрать?: '))

for number in range(quantity):
    song = input(f'Название {number + 1} песни: ')
    for one_song in violator_songs:
        if song == one_song[0]:
            time_all += one_song[1]

print('Общее время звучания песен: ', round(time_all, 2))
