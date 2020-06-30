from users import User
class Admin(User):
    def __init__(self,first_name,last_name,login_attempts):
        super().__init__(first_name,last_name,login_attempts)
        self.privileges = ["can add post","can delete post","can ban user","can warning user"]

    def show_privileges(self):
        print("\nAdministrator's set of privileges:")
        for items in self.privileges:
            print("\t-",items)

admin = Admin("Mayur","Patil",1)
admin.greet_user()
admin.describe_user()
admin.show_privileges()
