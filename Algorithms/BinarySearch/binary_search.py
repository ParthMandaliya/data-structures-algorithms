def binary_search(data, value):

    length = len(data)
    start, end = (0, length)
    mid_point = length // 2

    while start <= end:

        if value > data[mid_point]:
            start = mid_point + 1

        elif value < data[mid_point]:
            end = mid_point - 1

        elif value == data[mid_point]:
            from_start = mid_point
            if from_start - 1 > 0:
                while data[from_start] == value:
                    from_start -= 1
                from_start += 1
            till_end = mid_point
            if till_end + 1 < length:
                while data[till_end] == value:
                    till_end += 1
                till_end -= 1
            if from_start != till_end != mid_point:
                return tuple(i for i in range(from_start, till_end+1))
            else:
                return mid_point

        mid_point = (start + end) // 2

    return -1

if __name__ == "__main__":
    data = [4, 10, 12, 21, 34, 54, 55, 76, 89]
    data = [1, 4, 6, 9, 11, 15, 15, 15, 15, 17, 21, 34, 34, 56]
    find = 56

    print ("Element found at position #{0}".format(binary_search(data, find)))