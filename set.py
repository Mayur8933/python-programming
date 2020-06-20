#Set have unique items and properties.
#set = {"v1","v2","v3"}

vowels = ["a","e","i","o","u","a","e","i","o","u"]

set_of_vowels = {"a","e","i","o","u","a","e","i","o","u"}

print("list: ",vowels)#list have duplicates
print("set: ",set_of_vowels)

#properties : it holds only unique ,set does not print duplicates items

print("length: ",len(set_of_vowels))
set_of_vowels.add("o")
print("set: ",set_of_vowels)

#set is very efficient / fast / optimized

vowels2="aeiou"
set_of_vowels2=set(vowels2)#create a set with all characters
print(set_of_vowels2)

persons = ["Erick","David","Lisa","Lisa","David"]
set_of_persons=set(persons)
print("set_of_persons: ",set_of_persons)

#set methods

set1=set("aeiou")
set2=set("hello")
print("set 1: ",set1)
print("set 2: ",set2)

print("union: ",set1.union(set2))#union of sets
print("intersection: ",set1.intersection(set2))#intersection
print("Difference: ",set1.difference(set2))#print values which are in set1 but not in set2 
