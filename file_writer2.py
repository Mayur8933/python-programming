filename = "files/guest_book.txt"
print(f"creating {filename}")

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
        print(f"Hello {name}!")
        print("Welcome sir!")
        print(f"{name} visited here\n")






