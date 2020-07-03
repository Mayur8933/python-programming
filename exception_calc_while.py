try:
    while True:
        num1 = input("Enter First Number: ")
        num2 = input("Enter Second Number: ")
        Addition = int(num1)+int(num2)
        print(f"Addition of two numbers is:{Addition}")
except ValueError as error:
    print("You Cannot pass 'str' instead of 'int'")

