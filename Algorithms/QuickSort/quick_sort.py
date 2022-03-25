
def lomuto_partition(data):
    pivot = len(data)
    p_index = data[0]


def swap(a, b, data):
    if a != b:
        data[a], data[b] = data[b], data[a]

def hoare_partition(data, start, end):
    pivot_index = start

    while start < end:

        while start < end and data[start] <= data[pivot_index]:
            start += 1

        while data[end] > data[pivot_index]:
            end -= 1

        if start < end:
            # Swapping start with end
            swap(start, end, data)

    swap(pivot_index, end, data)

    return end

def lomuto_partition(data, p_index, end):
    pivot_index = end
    i = p_index

    while p_index <= end and i <= end:

        while data[p_index] < data[pivot_index]:
            p_index += 1

        i = p_index 

        while data[i] > data[pivot_index]:
            i += 1

        swap(p_index, i, data)
        p_index += 1

    return i

def quick_sort(data, start, end, partion_method="hoare"):
    if partion_method == "hoare" and start < end:
        pi = hoare_partition(data, start, end)
        quick_sort(data, start, pi - 1, partion_method)
        quick_sort(data, pi + 1, end, partion_method)
    if partion_method == "lomuto" and start < end:
        pi = lomuto_partition(data, start, end)
        quick_sort(data, start, pi-1, partion_method)
        quick_sort(data, pi+1, end, partion_method)


if __name__ == "__main__":
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')