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
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        shell_sort(arr)
        print("Sorted:", arr)
        # break
