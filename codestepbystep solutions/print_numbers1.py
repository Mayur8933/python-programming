def print_numbers1():

    for i in range(1,5+1):
        for j in range(i):
            print(i,end="")
            j += 1
        print()

print_numbers1()