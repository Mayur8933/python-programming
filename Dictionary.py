#dictionary is collection of key-value pairs

students = { "key1":"value1" ,"key2":"value2","key3":"value3" } #general syntax of dictionary
print(students)

alien = {"color":"green","points":100}
print(alien)

#keys are unique

print(alien.get("color"))
print(alien["color"])

alien["red"] = 200
alien["black"] = 150
alien["yellow"] = "color"
print(alien)

print("__"*30)

color = {} #empty dictionary
color = {"green":100}
color["red"] = 200
color["black"] = 90
print(color)

#access the value
print(color["black"])

#modify the value

color["red"]=500
print(color)

#remove the value
del color["green"]
print(color)

print("__"*30)

#loop through all key/value pairs

for key,value in color.items():
    print(key,value)

print("__"*30)

for key in color.keys():
    print(key)

print("__"*40)

for key in sorted(color.keys()):
    print(key)

print("__"*40)

for value in color.values():
    print(value)

print("__"*40)

persons = {"Allison":18 , "Benson":48 , "Paul":28 , "Erik":20, "Grace":25}
print(persons)

persons["stuart"]=98
print(persons)

#when we add entries in dictionary order is not maintained
#order is random

#key must be initialized = ""

persons[""] = 34
print(persons)

#why dict is so important data structure
#dictionary lookup is very fast

if "Paul" in persons.keys():   #membership
    print("paul's age",persons["Paul"])


