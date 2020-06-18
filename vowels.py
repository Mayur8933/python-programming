#write a program to count number of vowels 

vowels = ["a","e","i","o","u"]

def frequency_count(word):
    found = {}
    for letter in word:
        if letter in vowels:
            found.setdefault(letter,0)
            found[letter]+=1
    print(found)

text = "mayur patil"
frequency_count(text)

# OR

def frequency_count(word):
    found = {}
    for letter in word:
        if letter in vowels:
            if letter in found.keys():
                found[letter] = found[letter]+1
            else:
                found[letter] = 1
    print(found)
    
text = "python language"
frequency_count(text)
