def index_of(list,item):

    if item in list:
        return list.index(item)
    if item not in list:
        return -1

index_of([1, 2, 3, 4, 5, 6, 7, 8],8)
