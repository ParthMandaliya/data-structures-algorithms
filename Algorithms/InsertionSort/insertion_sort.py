def swap(a, b, data):
    if a != b:
        data[a], data[b] = data[b], data[a]

def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(0, i):
            if data[j] > data[i]:
                swap(i, j, data)

if __name__ == "__main__":
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [25, 39, 40, 25],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')