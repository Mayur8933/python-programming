class BankAccount:

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            return 0
        self.balance = self.balance + amount
        print("Deposited Amount: ",self.balance)

    def withdraw(self,amount):
        if amount < 0:
            return 0
        if amount > self.balance:
            return 0
        else:
            self.balance -= amount
            print("Withdraw Amount :",self.balance)


ba = BankAccount("Mayur")
ba.deposit(5.0)
ba.deposit(5.0)
ba.deposit(15.0)
ba.deposit(35.5)
ba.deposit(5.0)
ba.deposit(20.0)
ba.deposit(50.0)
ba.deposit(100.0)
ba.withdraw(12.0)
ba.withdraw(40.5)
ba.withdraw(100.0)








