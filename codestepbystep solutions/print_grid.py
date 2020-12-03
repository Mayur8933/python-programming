def print_grid(row,cols):
    for i in range(1,row+1):
        for j in range(1,cols+1):
            if j == (cols+1 - 1):
                print(i,end=" ")
            else:
                print(i,end=", ")
            i += row
        print()
print_grid(3,6)