# TODO здесь писать код
def tpl_sort(lst):
    for i in lst:
        if isinstance(i, int) == False:
            print(isinstance(i, int))
            return lst
    else:
        new_tpl_sort = list(lst)
        return tuple(sorted(new_tpl_sort))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))

# зачтено
