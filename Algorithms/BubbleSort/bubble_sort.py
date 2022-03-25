def bubble_sort(data):
    size = len(data)
    sorting = False

    for i in range(size-1):    
        for j in range(size-1-i):
            if data[j] > data[j+1]:
                # Swapping without third variable
                # a = 5, b = 2
                # a = a + b // a = 5 + 2 = 7
                # b = a - b // b = 7 - 2 = 5
                # a = a - b // a = 7 - 5 = 2 Swapped!
                data[j] = data[j]+data[j+1]
                data[j+1] = data[j]-data[j+1]
                data[j] = data[j]-data[j+1]
                sorting = True
        if not sorting:
            break
    return sorting


if __name__ == "__main__":
    data = [12, 4, 76, 34, 89, 54, 10, 21, 54]
    print ("Already sorted") if not bubble_sort(data) else print ("Sorted by QuickSort")
    print (data)