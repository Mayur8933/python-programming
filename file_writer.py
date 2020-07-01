filename = "files/respond_name.txt"

print(f"Creating {filename}...")
with open(filename,"w") as file_object:
    name1 = input("What is your name?\n")
    name2 = input("What is your name?\n")
    file_object.write(f"My name is {name1}\n")
    file_object.write(f"My name is {name2}")
