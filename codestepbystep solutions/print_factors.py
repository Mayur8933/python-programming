def print_factors(n):

    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")
            if i == n:
                break
            print("and",end=" ")

print_factors(24)