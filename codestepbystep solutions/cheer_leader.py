def cheerleader(lines, cheers):
    for line in range(lines):
        for space in range(line):
            print("   ", end="")
        for cheer in range(1, cheers):
            print("Go Team ", end="")
        print("Go")

cheerleader(3,6)



