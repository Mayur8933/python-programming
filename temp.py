filename = "files/tempfile.txt"
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError as error:
    print("I am done reading a file",error.filename)