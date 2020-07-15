def ascii_figure2(HEIGHT, HEIGHT2):
    
   
    slash_count1 = 8
    star_count1 = 0
    for i in range(0,HEIGHT):
        print("/" * slash_count1, "*" * (star_count1 * 8), "\\" * slash_count1,sep="")
        slash_count1 = slash_count1 - 4
        star_count1 = star_count1 + 1
    
    slash_count2 = 20
    star_count2 = 0
    for E in range(0,HEIGHT2):
        print("/" * slash_count2, "*" * (star_count2 * 8), "\\" * slash_count2,sep="")
        slash_count2 = slash_count2 - 4
        star_count2 = star_count2 + 1
        
ascii_figure2(3,6)
