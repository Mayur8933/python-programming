class user:

    def __init__(self,first_name,last_name,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.job = "Manager"
        self.salary = "1500k"
        self.login_attempts = login_attempts


    def describe_user(self):
        print("---USERS INFORMATION---")
        print(f"Users First Name: {self.first_name}")
        print(f"Users Last Name: {self.last_name}")
        print(f"Users Job: {self.job}")
        print(f"Users Salary: {self.salary}")
        print(f"Users Login Attempts: {self.login_attempts}")

    def greet_user(self):
         print("\t\tHELLO!")
         print(f"\tWELCOME , {self.first_name}")

    def increment_login_attempts(self):
         print(f"Number of Login Attempts: {self.login_attempts}")
         self.login_attempts += 1

    def reset_login_attempts(self,reset):
        print(f"Reset the Login attempts :{reset}\n")


first_user = user("James","Smith",2)
first_user.greet_user()
first_user.describe_user()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.reset_login_attempts(0)

second_user = user("Michael","Smith",4)
second_user.greet_user()
second_user.describe_user()
second_user.increment_login_attempts()
second_user.increment_login_attempts()
second_user.increment_login_attempts()
second_user.reset_login_attempts(0)


third_user = user("Robert","Smith",3)
third_user.greet_user()
third_user.describe_user()
third_user.increment_login_attempts()
third_user.increment_login_attempts()
third_user.increment_login_attempts()
second_user.reset_login_attempts(0)
