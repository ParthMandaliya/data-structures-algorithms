def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted_arrays(left, right)

def merge_sorted_arrays(arr_1, arr_2):
    len_a = len(arr_1)
    len_b = len(arr_2)

    sorted_array = []
    i = j = 0

    while i < len_a and j < len_b:
        if arr_1[i] <= arr_2[j]:
            sorted_array.append(arr_1[i])
            i+=1
        else:
            sorted_array.append(arr_2[j])
            j+=1

    while i < len_a:
        sorted_array.append(arr_1[i])
        i+=1
    while j < len_b:
        sorted_array.append(arr_2[j])
        j+=1

    return sorted_array

if __name__ == '__main__':
    b = [4, 9, 15, 90, 125, 272, 1997, 78,]
    a = [1, 52, 79, 80 ]

    print (merge_sort(b))
    # print (merge_sorted_arrays(a, b))

    # test_cases = [
    #     [10, 3, 15, 7, 8, 23, 98, 29],
    #     [],
    #     [3],
    #     [9,8,7,2],
    #     [1,2,3,4,5]
    # ]

    # for arr in test_cases:
    #     merge_sort(arr)
    #     print(arr)