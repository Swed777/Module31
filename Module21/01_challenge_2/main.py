# TODO здесь писать код

def pr_num(i, num):
    if i == num + 1:
        return
    else:
        print(i)
        pr_num(i + 1, num)

num = int(input('Введите num: '))
i = 1
pr_num(i, num)