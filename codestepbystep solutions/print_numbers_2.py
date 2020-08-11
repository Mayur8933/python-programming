def print_numbers2():
    dot = 4
    num = 1
    for i in range(5):

        for j in range(5):
            print("." * dot, f"{num}"*num ,sep="")
            break
        dot = dot - 1
        num = num +1
print_numbers2()