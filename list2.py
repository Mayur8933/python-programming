cars = ["bmw","audi","toyota","subaru"]

#sort a list by alphabetical order

cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

print(sorted(cars))

print(cars)

cars.reverse()
print(cars)

for car in cars:
    print(car.title())

for number in [1,2,4,2]:
    print(number)

print("____________")    

numbers = [11,232,6,7,15]

smallest_number = min(numbers)
print(smallest_number)

biggest_number = max(numbers)
print(biggest_number)

print("_____________")

print("sum of all numbers:",sum(numbers))

#list comprehensions allows to generate a list using some code

#list of squares for numbers:1-10
# **exponent

squares = [x**2 for x in range(1,11)]
print(squares)

for x in range(1,11):
    print(x**2)

cubes = [x**3 for x in range(1,11)]
print(cubes)
    
#slice of list (part of the list)

print("cubes of first 5 numbers is :",cubes[0:5])#0,1,2,3,4
print("cubes of numbers from 2-4",cubes[1:4])#0,1,2,3,4

start = 0
end = 6

print(cubes[:end])
print(cubes[4:])

print(cubes[:])  #<----all the elements

#slice of last 3 numbers in a list

print(cubes[-3:])
print(cubes[-3:-1])

for numbers in cubes[4:8]:
    print(numbers)

#copying a list

squares2=squares
print(squares2)
squares[0]=9999
print("squares:",squares)
print("squares:",squares2)

squares3=squares[:]
print(squares3)
squares[0]=1111
print(squares)
squares[5]=4232
print(squares)

#list in python are mutable(changeable):that means you can change the list(modify)
#tuple is immutable <-- you cannot change values

x = (2,4)#using round bracket is a tuple
print(x)
print(x[0])#accessing the value
for i in x:
    print(i)

x=(3,9)#types are dynamic
print(x)
    

    
    




