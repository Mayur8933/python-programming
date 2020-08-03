def matrix_add(list1, list2):
    matrix_c = []

    for i in range(len(list1)):
        empty = []
        for j in range(len(list2[0])): # here length of list2[0] is 3 ,so 2nd for loop executes 3 times and append value to the empty list.
            list_ij = list1[i][j] + list2[i][j]
            empty.append(list_ij)
        matrix_c.append(empty)
    print(matrix_c)

matrix_add([[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]])
matrix_add([[1, 2, 3], [4, 4, 4]], [[5, 5, 6], [0, -1, 2]])
