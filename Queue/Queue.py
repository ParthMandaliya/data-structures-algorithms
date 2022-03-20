from collections import deque #Pronounced 'deck'

# Last in first out (LIFO)
class Queue():
    def __init__(self):
        self.__container = deque()

    def enqueue(self, value):
        self.__container.appendleft(value)

    def dequeue(self):
        return self.__container.pop()

    def peek(self):
        return self.__container[0]

    def is_empty(self):
        return len(self.__container) == 0

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        temp = []
        for ele in self.__container:
            temp.append(ele)
        return f'Queue({temp})'

if '__main__' == __name__:
    obj = Queue()
    obj.enqueue({'five': 5})
    obj.enqueue({'six': 6})
    obj.enqueue({'fifteen': 15})
    obj.enqueue({'twenty': 20})
    obj.enqueue({'eight': 8})
    print (obj)
    print (obj.dequeue())