from restaurant2 import Restaurant2
class IceCreamStand(Restaurant2):
    def __init__(self,resturant_name ,cuisine_type):
        super().__init__(resturant_name ,cuisine_type)
        self.flavors = ["chocolate","vanilla","butterscotch","mango"]

    def dislpay_flavors(self):
        print("LIST OF ICE-CREAM FLAVORS:")
        for items in self.flavors:
            print(f"\t{items.upper()} Ice-cream")

my_resto = IceCreamStand("Delicious","Indian")
my_resto.describe_restaurant()
my_resto.open_restaurant()
my_resto.dislpay_flavors()

