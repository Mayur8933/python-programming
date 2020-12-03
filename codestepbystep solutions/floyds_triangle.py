def floyds_triangle(n):
    k= 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(k,end=" ")
            k = k + 1
        print()

floyds_triangle(5)