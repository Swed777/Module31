nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# TODO здесь писать код
# print([x for x in nice_list])                 Тренировка
# print([y for x in nice_list for y in x])      Треннировка

print([y for x in nice_list for y in [a for b in x for a in b]])
