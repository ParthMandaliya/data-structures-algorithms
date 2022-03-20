class HashTable:
    def __init__(self) -> None:
        self.__max = 100
        self.__length = 0
        self.__arr = [[] for i in range(self.__max)]

    def __get_hash(self, key):
        n = 0
        for i in key:
            n += ord(i)
        return n % self.__max

    def add(self, key, value):
        hash = self.__get_hash(key)
        
        for idx, element in enumerate(self.__arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.__arr[hash][idx] = (key, value)
                return
        self.__arr[hash].append((key, value))
        self.__length += 1

    def __setitem__(self, key, value):
        self.add(key, value)

    def get(self, key):
        hash = self.__get_hash(key)
        try:
            for element in self.__arr[hash]:
                if element[0] == key:
                    return element[1]
        except IndexError:
            return

    def __getitem__(self, key):
        return self.get(key)

    def remove(self, key):
        hash = self.__get_hash(key)
        for idx, element in enumerate(self.__arr[hash]):
            if element[0] == key:
                del self.__arr[hash][idx]
                self.__length -= 1
                return

    def __contains__(self, key):
        hash = self.__get_hash(key)
        for idx, element in enumerate(self.__arr[hash]):
            if element[0] == key:
                return True
        return False

    def __delitem__(self, key):
        self.remove(key)

    def __str__(self):
        return str(self.__arr)

    def __len__(self):
        return self.__length

if __name__ == "__main__":
    obj = HashTable()
    obj['march 6'] = 130
    obj['march 7'] = 140.5
    obj['march 17'] = 130.28
    obj['march 9'] = 128
    
    print ("march 9 in obj:", 'march 9' in obj)

    print (obj['march 6'])
    print (obj['march 7'])
    print (obj['march 17'])
    print (obj['march 9'])
    
    print (f"Length of hash table: {len(obj)}")
    
    del obj['march 7']
    del obj['march 17']

    print (f"Length of hash table: {len(obj)}")
    del obj['march 6']
    print (f"Length of hash table: {len(obj)}")