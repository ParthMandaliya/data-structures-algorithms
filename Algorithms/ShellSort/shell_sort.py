def swap(a, b, data):
    if a != b:
        data[a], data[b] = data[b], data[a]


def shell_sort(data, gap_i=2):
    gap = len(data)//gap_i
    if gap > 0:
        spaces = [i for i in range(0, len(data), gap)]
        for i in range(0, len(spaces)):
            for j in range(0, i):
                if data[i] < data[j]:
                    swap(i, j, data)
        gap_i *= 2
        gap = len(data)//(gap_i)
        shell_sort(data, gap_i)


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    elements = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
    for elements in tests:
        shell_sort(elements)
        print(elements)