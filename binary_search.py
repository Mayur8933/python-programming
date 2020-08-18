def binary_search(item_list,item):
    low = 0
    high = len(item_list) - 1
    mid = 0

    while low <= high:
        mid = (high+low)//2
        if item_list[mid] < item:
            low = mid + 1
        elif item_list[mid] > item:
            high = mid - 1
        else:
             return mid
    return -1

result = binary_search([10,20,30,40,50,60],50)

if result != -1:
    print("Item is present at index", result)
else:
    print("Item not present")


