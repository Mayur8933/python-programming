class Restaurant2:
    def __init__(self,resturant_name ,cuisine_type):
        self.restaurant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("-----My Restaurant details------")
        print(f"\tRestaurant Name: {self.restaurant_name}")
        print(f"\tCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\tRestaurant {self.restaurant_name} is open now.\n")

    def set_number_served(self,):
        print(f"Number of customers served are : {self.number_served}")

    def increment_number_served(self,customers):
        print(f"This Restuarant has {customers} customers")
        self.number_served += customers

restaurant = Restaurant2("DHABA","Indian Cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()

another_restaurant = Restaurant2("BUZZ-TIME","American Cuisine")
another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()

another_restaurant2 = Restaurant2("CHILL-OUT","Italian Cuisine")
another_restaurant2.describe_restaurant()
another_restaurant2.open_restaurant()

