import os
temp = f"{'/'.join(os.path.abspath(__file__).split('/')[:-2])}/common"
import sys
sys.path.append(temp)

from node import Node

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__length = 0

    def __insert_first_node(self, data):
        node = Node(data)
        node.next = node
        node.prev = node
        self.head = self.tail = node
        self.__length += 1

    def insert_at_begining(self, data):
        if self.head == self.tail == None:
            self.__insert_first_node(data)
            return
        node = Node(data, self.head, self.tail)
        self.tail = self.head.prev
        self.tail.next = node #self.head
        self.head.prev = node
        self.head = node
        self.__length += 1

    def insert_at_end(self, data):
        if self.head == self.tail == None:
            self.__insert_first_node(data)
            return
        node = Node(data, self.head, self.tail)
        self.tail.next = node
        self.tail = node
        self.head.prev = self.tail
        self.__length += 1

    def insert_at(self, index, data) :
        if index < 0 or index > len(self):
            raise IndexError(f"Size of the linked list is {len(self)}, passed index {index}")
        if index == 0:
            self.insert_at_begining(data)
            return
        elif index == len(self):
            self.insert_at_end(data)
            return

        itr = self.head
        counter = 0
        while counter < index-1:
            itr = itr.next
            counter += 1
        node = Node(data, itr.next, itr)
        itr.next.prev = node
        itr.next = node
        self.__length += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def __len__(self):
        return self.__length

    def tolist(self):
        llist = []
        itr = self.head
        while True:
            llist.append(itr.data)
            if itr == self.tail:
                break
            itr = itr.next
        return llist

    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        llstr = ''
        itr = self.head
        while True:
            if itr == self.head:
                llstr += f"*TAIL <--> {str(itr.data)} <--> "
            elif itr == self.tail:
                llstr += f"{str(itr.data)} <--> *HEAD"
            else:
                llstr += f"{str(itr.data)} <--> "
            if itr == self.tail:
                break
            itr = itr.next
        return llstr

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_begining("apple")
    dll.insert_at_end("mango")
    dll.insert_at_end("blueberry")

    print ("-"*20)
    print ("-"*20)
    print ("length of doublylinked list:", len(dll))
    print ("-"*20)
    print ("-"*20)
    print (dll)
    print ("-"*20)
    print ("head.data:", dll.head.data)
    print ("head.prev.data:", dll.head.prev.data)
    print ("head.next.data:", dll.head.next.data)
    print ("-"*20)
    print ("tail.data:", dll.tail.data)
    print ("tail.prev.data:", dll.tail.prev.data)
    print ("tail.next.data:", dll.tail.next.data)
   
    print ("-"*20)
    print ("-"*20)

    dll.insert_at(0, "banana")
    print (dll)
    print ("-"*20)
    print ("head.data:", dll.head.data)
    print ("head.prev.data:", dll.head.prev.data)
    print ("head.next.data:", dll.head.next.data)
    print ("-"*20)
    print ("tail.data:", dll.tail.data)
    print ("tail.prev.data:", dll.tail.prev.data)
    print ("tail.next.data:", dll.tail.next.data)

    print ("-"*20)
    print ("-"*20)
    
    dll.insert_at(len(dll), "jackfruit")
    print (dll)
    print ("head.data:", dll.head.data)
    print ("head.prev.data:", dll.head.prev.data)
    print ("head.next.data:", dll.head.next.data)
    print ("-"*20)
    print ("tail.data:", dll.tail.data)
    print ("tail.prev.data:", dll.tail.prev.data)
    print ("tail.next.data:", dll.tail.next.data)
    
    print ("-"*20)
    print ("-"*20)
    
    dll.insert_at(2, "peach")
    print (dll)
    print ("-"*20)
    print ("-"*20)

    print (dll.tolist())