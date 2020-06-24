def sandwich(name,*list_of_items):
    """print the list of items on sandwich which are requested"""
    print(f"Sandwich Name:{name}")
    print(f"Items on sandwich : {list_of_items}\n")
sandwich("Paneer","Tomato","Paneer","Onion")
sandwich("Veg","Onion","Cucumber","Tomato")
sandwich("Chicken","Cheese","Lettuce","chicken")

print("\n-----Sanwiches that was ordered------")
Name_of_sandwich = ["Paneer","Veg","Chicken"]
for Each_sandwich in Name_of_sandwich:
     print(f"\n-{Each_sandwich} Sandwich ")
       
