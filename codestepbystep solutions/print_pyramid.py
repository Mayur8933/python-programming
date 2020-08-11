def pyramid():
    space1 = 5
    space2 = 5
    star = 1
    for i in range(6):
        for j in range(11):
            print(" " * space1 , "*" * star , " " * space2)
            break
        space1 = space1 - 1
        space2 = space2 - 1
        star = star + 2
pyramid()