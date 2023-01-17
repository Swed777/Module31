# TODO здесь писать код
def tpl_sort(lst):
    new_tpl_sort = list(lst)
    return tuple(sorted(new_tpl_sort))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
print(tpl_sort((6, 3, -1, 8, 12.4, 10, -5)))
print(tpl_sort((6, 3, -1, 8, 4, "d", -5)))

