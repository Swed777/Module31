# TODO здесь писать код
import random

first = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Первая команда: ', first)
second = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Вторая команда: ', second)
winners = [float(first[i])  if first[i] > second[i] else float(second[i]) for i in range(20)]
print('Победители тура', winners)