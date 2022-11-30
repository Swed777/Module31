data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


# TODO здесь писать код

print('---------------------------------------------------')
print('1. Выводим и ключи, и значения словаря:', data)           #  Выводим список и ключей,  и значений словаря
print('   Выводим только ключи:               ', data.keys())       # Выводим только ключи словаря
print('   Выводим только значения:            ', data.values())     # Выводим только значения словаря

print('---------------------------------------------------')
data["ETH"]["total_diff"] = 100                                  # Добавляем ключ “total_diff” со значением 100
print('2. Выполнененое задание № 2:           ', data["ETH"])

print('---------------------------------------------------')
data["tokens"][0]["fst_token_info"]["name"] = "doge"
print('3. Выполненное задание  № 3:           ', data["tokens"][0]["fst_token_info"])   # Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.

print('---------------------------------------------------')
    # Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.

    # ?????  НИКИТА  - поясните это задание (№ 4) плз - “total_out” в "tokens" есть в двух местах, с одинаковым значением = 0.
    # Удалить его нужно в обоих местах? и да, сейчас  оба значения равны 0, поэтому в ETH можно перенести любое. Но как быть и то переносить, если значения “total_out” были бы разные?
    # Получается - условие некорректно прописано?
data["ETH"]["total_out"] = data["tokens"][0].pop("total_out")
data["tokens"][1].pop("total_out")
print('4а. Выполненное задание № 4:           ', data["tokens"][0])
print('4б. Выполненное задание № 4:           ', data["ETH"])

print('---------------------------------------------------')
data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"].pop("price")  # Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
print('5. Выполненное задание № 5:            ', data["tokens"][1]["sec_token_info"])


'''
Списки ключей и значений словара:
При работе с API (application programming interface) сайта биржи по криптовалюте вы получили вот такие данные в виде словаря:

 Напишите программу, которая выполняет следующий алгоритм действий:
1. Вывести списки ключей и значений словаря.
2. В “ETH” добавить ключ “total_diff” со значением 100.
3. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
4. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
5. Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
'''