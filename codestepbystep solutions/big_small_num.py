num = int(input("How many numbers? "))
big = 0
small = 0
for i in range(num):
    num2 = int(input("Next number? "))
    if num2 > big:
        big = num2
    else:
        small = num2
print("big", big)
print("small", small)


