from users import User
class Admin(User):
    def __init__(self,first_name,last_name,login_attempts):
        super().__init__(first_name,last_name,login_attempts)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges_items = ["can add post", "can delete post", "can ban user", "can warning user"]

    def describe_privileges(self):

        print("\nAdministrator's set of privileges:")
        for items in self.privileges_items:
            print("\t-",items)

admin2 = Admin("Mayur","Patil",1)
admin2.greet_user()
admin2.describe_user()
admin2.privileges.describe_privileges()



