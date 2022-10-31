shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код

name_detail = input('Название детали: ')
count_name = 0
price_sum = 0

for detail in shop:
        for name in detail:
                if name == name_detail:
                        count_name += 1
                        price_sum += detail[1]

print(f'Количество деталей {name_detail} - {count_name} \nОбщая стоимость - {price_sum}')
