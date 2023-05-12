# TODO здесь писать код
class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None

    def __str__(self):
        return 'Node [{value}]'.format(value=str(self.value))


class LinkedList:
    def __init__(self):
        self.head = None
        self.lengh = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            value = [str(current.value)]
            while current.nxt is not None:
                current = current.nxt
                value.append(str(current.value))
            return '[{value}]'.format(value=' '.join(value))
        return 'LinkedList []'

    def append(self, element):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.nxt:
            last = last.nxt
        last.nxt = newNode
        self.lengh += 1

    def index_check(self, index):
        if not 0 <= index <= self.lengh:
            raise IndexError

    def get(self, index):
        self.index_check(index)
        current = self.head
        for _ in range(index):
            current = current.nxt
        return current.value

    def remove(self, index):
        curNode = self.head
        curIndex = 0

        if curNode is not None:
            if index == 0:
                self.head = curNode.nxt
                self.lengh -= 1
                return
        while curNode is not None:
            if curIndex == index:
                break
            prev = curNode
            curNode = curNode.nxt
            curIndex += 1
        self.lengh -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

# зачтено
