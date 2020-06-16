cars = ["audi","bmw","lexus","ford"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

if "bm4" in cars:
    print("I have BMW in list")
else:
    print("no bmw")

print("___________________")
#admission fee for park
#age<4:free
#4-18:25
#>18:40

age = int(input("Enter The Age:"))
if age<4:
    print("admission fee is 0RS.")
elif age<18:
    print("admission fee is 25RS.")
elif age<65:
    print("admission fee is 40RS.")
else:
    print("admission fee is 0RS.")
print("_____________________")

#age<4,>65 ----fee 0

if age<4 and age>65:
    print("free")


    
    
