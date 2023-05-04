# TODO здесь писать код

class Stack:
    def __init__(self):
        self.items = []

    def add_elem(self, item: list):
        self.items.append(item)

    def pop(self, index: int):
        removed = self.items.pop(index)
        return removed

    def __str__(self):
        return f'{self.items}'


class TaskManager:
    def __init__(self, task: str, priority: int = 0):
        self.task = ('task', priority)

    def __str__(self):
        return f'Задача: {self.task}, Приоритет: {self.priority}'


st = Stack()
st.add_elem(("сделать уборку", 4))
st.add_elem(("помыть посуду", 4))
st.add_elem(("отдохнуть", 1))
st.add_elem(("поесть", 2))
st.add_elem(("сдать ДЗ", 2))
# print(st)
# st.pop(2)
# print(st)

# Сделать сортировку
st_sort = sorted(st.items, key=lambda x: x[1])

print('Результат:')
for key, value in st_sort:
    print(f'{value} - {key}')

# зачтено
