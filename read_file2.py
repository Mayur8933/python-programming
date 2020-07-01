# replacing words

file_path = "files/learning_python.txt"
with open(file_path) as file_object:
    print("Contents of the file is:")
    for line in file_object:
        print(line.replace('Python','C').strip())
