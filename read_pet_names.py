#reading cat names

filename = "files/cats.txt"
try:
    with open(filename) as file_object:
        content = file_object.read()
    print(f"Cats names are :\n{content}")
except FileNotFoundError as error:
    print("File not found",error.filename)

print("I am done reading a file\n")


#reading dog names
filename2 = "files/dogs.txt"
try:
    with open(filename2,"r") as file_object2:
        content2 = file_object2.read()
    print(f"Dogs names are :\n{content2}".strip())
except FileNotFoundError as error2:
    print("File not found",error2.filename)

print("I am done reading a file")