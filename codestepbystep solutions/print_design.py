def fun():
    count = 5
    num = 1
    x = 1
    for i in range(5):
        for j in range(11):
            print("-" * count,end="")
            print(f"{num}" * x,end="")
            print("-" * count)
            break
        count = count - 1
        num = num + 2
        x = x + 2
fun()