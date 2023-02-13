# TODO здесь писать код
def summ(*args):
    def element(data):
        result = []
        for i_elem in data:
            if isinstance(i_elem, int):
                result.append(i_elem)
            else:
                result.extend(element(i_elem))
        return result

    return sum(element(args))


result = summ([[1, 2, [3]], [1], 3])
print('Ответ:', result)
result = summ(1, 2, 3, 4, 5)
print('Ответ:', result)

# зачтено
