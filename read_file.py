#reading an entire file
print("---Reading an Entie File---")
with open("files/learning_python.txt") as file_object:
    contents = file_object.read()
print("Contents of the file is:\n",contents.rstrip(),"\n-------\n")

#reading a file with looping over file object
print("---Reading file with looping over file object---")
learn_py = ""
file_path = "files/learning_python.txt"
with open(file_path) as file_object:
    for line in file_object:
        learn_py += line
print(f"Contents of the file is:\n{learn_py}\n")

#reading a file with storing in a list and then working with them
print("---Reading an file with storing in a list ---")
with open(file_path) as file_object:
    lines = file_object.readlines()
no_of_lines = len(lines)
print("no of lines : ",no_of_lines)
for i in range(no_of_lines):
    print(lines[i].strip())




