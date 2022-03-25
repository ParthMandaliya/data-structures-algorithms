def bubble_sort(data, sorting_key):
    size = len(data)
    sorting = False

    for i in range(size-1):    
        for j in range(size-1-i):
            if data[j][sorting_key] > data[j+1][sorting_key]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                sorting = True
        if not sorting:
            break

if __name__ == "__main__":
    elements = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
    bubble_sort(elements, "name")
    print (elements)