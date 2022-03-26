def find_min(data):
    min = 0
    for i in range(len(data)):
        if data[min] > data[i]:
            min = i

    return min

def swap(a, b, data):
    if a != b:
        data[a], data[b] = data[b], data[a]

def selection_sort(data):
    for i in range(len(data)-1):
        min = find_min(data[i:])
        swap(i, min+i, data)

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]

    for elements in tests:
        selection_sort(elements)
        print(elements)