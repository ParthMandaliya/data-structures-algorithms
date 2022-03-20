from collections import deque #Pronounced 'deck'

class Stack():
    def __init__(self):
        self.__container = deque()

    def push(self, value):
        self.__container.append(value)

    def pop(self):
        return self.__container.pop()

    def peek(self):
        return self.__container[-1]

    def is_empty(self):
        return len(self.__container) == 0

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        temp = []
        for ele in self.__container:
            temp.append(ele)
        return f'Stack({temp})'

if '__main__' == __name__:
    obj = Stack()
    obj.push(5)
    obj.push(6)
    obj.push(15)
    obj.push(20)
    obj.push(8)
    print (obj.pop())
    print (obj)