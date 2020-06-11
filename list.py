cities = []
print(cities)
cities = ["sanjose","Las Vegas","Mumbai"]
print(cities)

cities.append("pune")
print(cities)

print("city : ",cities[2])
cities.append("dhule")
print(cities)

cities.remove("dhule")
print(cities)

print("last item:",cities[-1])
print(cities)

for city in cities:
    print(city)

for index,city in enumerate(cities):
    print(cities[index])

#grow a list at runtime using append
#remove an item : remove
    
print(len(cities))

if "pune"in cities:
    print("pune is there")
    
if "delhi" not in cities:
    cities.append("delhi")
    
print(cities)
del cities[3]

print(cities)

#cities.remove(3)  <-- not declare like this

#stack data structure <-- Last in First out

cities.append("Nashik") #push(Adding)
print(cities)

cities.pop() #removing
print(cities)

last_item = cities.pop()
print(last_item)

cities.extend(["a","b","c"])#extend list with new items
print(cities)

cities.insert(4,"Lake Tahoe")
print(cities)

cities.sort()
print(cities)

cities.reverse()
print(cities)

print(cities[4])

print(cities.index("Mumbai"))

cities.copy()
print(cities)





