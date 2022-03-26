import os
temp = f"{'/'.join(os.path.abspath(__file__).split('/')[:-2])}/common"
import sys
sys.path.append(temp)

from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        itr = self.head
        llstr = ''
        while itr:
            llstr += f"{str(itr.data)} --> " if itr.next else str(itr.data)
            itr = itr.next
        return llstr

    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>len(self):
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=len(self):
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                self.insert_at(count+1, data_to_insert)
                return
            itr = itr.next
            count += 1
        raise Exception(f"{data_after} value not found")

    def index(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                return count
            count += 1
            itr = itr.next
        raise Exception(f"{data} not found in the linked list")

    def __contains__(self, data):
        try:
            self.index(data)
            return True
        except Exception:
            return False

    def remove_by_value(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                return
            itr = itr.next
            count += 1
        raise Exception(f"{data} value not found")
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    print (ll)

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    print (ll)

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes", "orange"])
    print (ll)
    ll.insert_after_value("mango","apple") # insert apple after mango
    print (ll)
    ll.remove_by_value("orange") # remove orange from linked list
    print (ll)
    print (f"Length of linked list: {len(ll)}")
    print (f"index of 'mango': {ll.index('mango')}")
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    print (f"'apple' in ll?: {'apple' in ll}")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes") 
    print (ll)