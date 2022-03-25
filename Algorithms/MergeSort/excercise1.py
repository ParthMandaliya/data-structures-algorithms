def merge_sort(arr, key, ascending=True):
    if len(arr) <= 1:
        return 

    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    merge_sort(left, key, ascending)
    merge_sort(right, key, ascending)

    merge_sorted_arrays(arr, key, left, right, ascending)

def merge_sorted_arrays(data, key, arr_1, arr_2, ascending=True):
    len_a = len(arr_1)
    len_b = len(arr_2)

    i = j = k = 0

    while i < len_a and j < len_b:
        if ascending:
            if arr_1[i][key] <= arr_2[j][key]:
                data[k] = arr_1[i]
                i+=1
            else:
                data[k] = arr_2[j]
                j+=1
        else:
            if arr_1[i][key] >= arr_2[j][key]:
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
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    # for arr in elements:
    merge_sort(elements, "age", True)
    print("Sorted:", elements)