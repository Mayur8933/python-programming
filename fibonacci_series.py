def fibonacci(n):
    first_num = 0
    second_num = 1
    count = 1
    sum = 0
    for i in range(1,n+1):
        print(sum,end=" ")
        count = count +1
        first_num = second_num
        second_num = sum
        sum = first_num + second_num
fibonacci(9)