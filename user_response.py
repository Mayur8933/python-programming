filename = "files/opinion.txt"
print(f"creating {filename}")

print("Enter 'quit' when you are finished.")
while True:
    response = input("\nWhy you like programing? ")
    if response == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(response + "\n")
