def merge_sort(arr):
    if len(arr) <= 1:
        return 

    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_arrays(arr, left, right)

def merge_sorted_arrays(data, arr_1, arr_2):
    len_a = len(arr_1)
    len_b = len(arr_2)

    i = j = k = 0

    while i < len_a and j < len_b:
        if arr_1[i] <= arr_2[j]:
            data[k] = arr_1[i]
            i+=1
        else:
            data[k] = arr_2[j]
            j+=1
        k+=1

    while i < len_a:
        data[k] = arr_1[i]
        i+=1
        k+=1

    while j < len_b:
        data[k] = arr_2[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print("Sorted:", arr)